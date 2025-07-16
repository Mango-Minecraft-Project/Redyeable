from pathlib import Path
from shutil import rmtree
import json
import tomllib

CWD = Path.cwd()
MAIN = CWD / "src/main"
GENERATED = CWD / "src/generated"

def get_metadata():
    if (forge_metadata := MAIN / "META-INF/mods.toml").is_file():
        with forge_metadata.open("rb") as file:
            return ("forge", tomllib.load(file))
    elif (neoforge_metadata := MAIN / "META-INF/neoforge.mods.toml").is_file():
        with neoforge_metadata.open("rb") as file:
            return ("neoforge", tomllib.load(file))
    elif (fabric_metadata := MAIN / "fabric.mod.json").is_file():
        with fabric_metadata.open("r", encoding="utf-8") as file:
            return ("fabric", json.load(file))
    else:
        raise FileNotFoundError(
            "No metadata file found. Please ensure META-INF/mods.toml, META-INF/neoforge.mods.toml or fabric.mod.json exists."
        )

loader_type, metadata = get_metadata()
if loader_type in {"forge", "neoforge"}:
    modId = metadata["mods"][0]["modId"]
else:
    modId = metadata["id"]

NAMESPACE = modId

COLORS = [
    "black",
    "blue",
    "brown",
    "cyan",
    "gray",
    "green",
    "light_blue",
    "light_gray",
    "lime",
    "magenta",
    "orange",
    "pink",
    "purple",
    "red",
    "white",
    "yellow",
]


def make_dir(original_path: Path, rmdir: bool = False) -> Path:
    """Create a directory if it does not exist."""
    path = original_path.parent if original_path.suffix else original_path
    if rmdir:
        rmtree(path, ignore_errors=True)
    path.mkdir(parents=True, exist_ok=True)
    return original_path

__all__ = ["CWD", "MAIN", "GENERATED", "NAMESPACE", "COLORS", "make_dir", "get_metadata"]