import datetime as dt
from pathlib import Path

import yaml
from addict import Dict

KST = dt.timezone(offset=dt.timedelta(hours=9), name="KST")
RESOURCES = Path("src") / "server" / "resources"

with open(RESOURCES / "config.yaml", encoding="utf-8") as f:
    config = Dict(yaml.load(f, Loader=yaml.SafeLoader))


with open(RESOURCES / config.fastapi.description) as f:
    description = f.read()
