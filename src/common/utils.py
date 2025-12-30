# helper functions

from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / 'configs'


def load_yaml_config(filename: str) -> dict:
    config_path = CONFIG_DIR / filename
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

