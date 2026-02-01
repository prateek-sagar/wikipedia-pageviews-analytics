from functools import wraps
from storage.save_observation import save_observation
def observable(action: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):


            run_id = kwargs.get("run_id")
            window = kwargs.get('window')

            status = "success"
            exception = None

            try:
                result = func(*args, **kwargs)
                return result
            
            except Exception as e:
                status = "failed"
                exception = str(e)
                raise
            
            finally: 

                observation = {
                    "identity": {
                        "run_id": run_id,
                        "window": window
                    },
                    "intent": {
                        "action": action
                    },
                    "observation": {
                        "status": status,
                        "exception": exception
                    }
                }
                save_observation(observation, run_id)
        return wrapper
    return decorator