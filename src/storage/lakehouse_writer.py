from datetime import date, datetime
import uuid
from functools import singledispatch
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / 'src'

# Evidence is capturing and refining the truth, on time and run basis. 
# Run is a task that performs 
@singledispatch
def evidence_writer(result, action) -> None:
    raise TypeError(f"Unsupported type: {type(result)}")

@evidence_writer.register
def _(result: dict, action) -> None:
    _write_file(action, json.dumps(result, indent=2), '.json')

@evidence_writer.register
def _(result: str, action) -> None:
    _write_file(action, result, ".txt")

def _write_file(action, content, suffix):
    date_str = date.today().strftime('%Y_%m_%d')
    run = datetime.now().strftime('%I_%M') + str(uuid.uuid4())

    file_path = (
        DATA_DIR / 'evidence' / date_str / run / action
    ).with_suffix(suffix)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "x") as f:
        f.write(content)
        