import json
from pathlib import Path

from starlette.config import Config

RESOURCES = Path("src") / "client" / "resources"

configs = Config(RESOURCES / ".env")

with open(RESOURCES / "api_description.md") as f:
    description = f.read()

with open(RESOURCES / "tags_metadata.json") as f:
    tags_metadata = json.load(f)["tags"]
