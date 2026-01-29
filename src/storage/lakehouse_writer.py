from datetime import date, datetime

from functools import singledispatch
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / 'src'

# Evidence is capturing and refining the truth, on time and run basis. 
# Run is a task that performs 
@singledispatch
def evidence_writer(result, action, run) -> None:
    raise TypeError(f"Unsupported type: {type(result)}")

@evidence_writer.register
def _(result: dict, action, run) -> None:
    
    result['run_id'] = run
    _write_file(run, generate_content(action, result), '.json')

@evidence_writer.register
def _(result: str, action, run) -> None:
    _write_file(run, result, ".txt")

def _write_file(run, content, suffix):
    date_str = date.today().strftime('%Y_%m_%d')

    file_path = (
        DATA_DIR / 'evidence' / date_str / run 
    ).with_suffix(suffix)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "x") as f:
        f.write(content)


def generate_content(action, result) -> dict:
    content = {
        "identity" : {
            "run_id": result.run_id,
            "window": {
                "start": result.start,
                "end": result.end
            }
        },
        "intent": {
            "action": action
        },
        "observation": {
            "status": result.status,
            "exception": result.exception
        }
    }

    return content