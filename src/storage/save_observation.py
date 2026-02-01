from datetime import date, datetime

from functools import singledispatch
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / 'src'

# Evidence is capturing and refining the truth, on time and run basis. 
# Run is a task that performs 
@singledispatch
def save_observation(observatoin, run) -> None:
    raise TypeError(f"Unsupported type: {type(observatoin)}")

@save_observation.register
def _(observation: dict, run) -> None:
    _write_file(observation, run, '.json')

@save_observation.register
def _(observation: str, run) -> None:
    _write_file( observation, run,  ".txt")

def _write_file(observation, run, suffix):
    date_str = date.today().strftime('%Y_%m_%d')

    file_path = (
        DATA_DIR / 'evidence' / date_str / run 
    ).with_suffix(suffix)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "x") as f:
        f.write(observation)
