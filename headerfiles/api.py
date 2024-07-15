import json
from importlib import resources

loaded = False
headerjson = None

def __load_headerfiles():
    global loaded, headerjson
    try:
        with resources.open_text('headerfiles.data', "headerfiles.json") as f:
            headerjson = json.load(f)
    except FileNotFoundError:
        print("ERROR: headerfiles.json not found")
        headerjson = {}
    loaded = True

def __get_headerfiles(proj: str) -> list[str]:
    global loaded, headerjson
    if not loaded:
        __load_headerfiles()
    return headerjson.get(proj, [])

def __get_supported_projects() -> set[str]:
    global loaded, headerjson
    if not loaded:
        __load_headerfiles()
    return set(headerjson.keys())


def is_supported_proj(proj: str) -> bool:
    """
    API function `is_supported_proj`
      - Usage: Check if a projection is supported by the API.
      - Return value: True if the projection is supported, False otherwise.
    """
    return proj in __get_supported_projects()

def get_proj_headers(proj: str) -> list[str]:
    """
    API function `get_proj_headers`
      - Usage: Get the inferred headers for a specific project.
      - Return value: A list of inferred headers for the project, their orders also matter.
    """
    global loaded, headerjson

    if not is_supported_proj(proj):
        return None

    return __get_headerfiles(proj)
