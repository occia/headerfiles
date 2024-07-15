import json

loaded = False
headerfiles = None

def __load_headerfiles():
    global loaded, headerfiles
    try:
        with open("headerfiles/headerfiles.json", "r") as f:
            headerfiles = json.load(f)
    except FileNotFoundError:
            headerfiles = {}
    loaded = True

def __get_headerfiles(proj):
    global loaded, headerfiles
    if not loaded:
        __load_headerfiles()
    return headerfiles.get(proj, [])


def is_supported_proj(proj):
    """
    API function `is_supported_proj`
      - Usage: Check if a projection is supported by the API.
      - Return value: True if the projection is supported, False otherwise.
    """
    return proj in [ 
        "libfdk-aac",
        "libfuse",
        "libpsl",
        "libsodium",
        "libtasn1",
        "libyal",
     ]

def get_proj_headers(proj):
    """
    API function `get_proj_headers`
      - Usage: Get the inferred headers for a specific project.
      - Return value: A list of inferred headers for the project, their orders also matter.
    """
    global loaded, headerfiles

    if not is_supported_proj(proj):
        return None

    return __get_headerfiles(proj)
