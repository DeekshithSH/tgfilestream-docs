import importlib
from os import environ
if (not environ.get("PUBLIC_URL")) and environ.get("RENDER_EXTERNAL_URL"):
    environ["PUBLIC_URL"]=environ.get("RENDER_EXTERNAL_URL")

importlib.import_module("tgfs.__main__")
