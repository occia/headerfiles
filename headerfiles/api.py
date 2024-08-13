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

def is_supported_proj(proj: str) -> bool:
    """
    API function `is_supported_proj`
      - Usage: Check if a projection is supported by the API.
      - Return value: True if the projection is supported, False otherwise.
    """
    global loaded, headerjson
    if not loaded:
        __load_headerfiles()
    return set(headerjson.keys())

def get_proj_headers(proj: str) -> list[str]:
    """
    API function `get_proj_headers`
      - Usage: Get the inferred headers for a specific project.
      - Return value: A list of inferred headers for the project, their orders also matter.
    """
    global loaded, headerjson
    if not loaded:
        __load_headerfiles()
    if proj not in headerjson:
        return []
    return headerjson[proj]["headers"]

def get_build_script(proj: str, install_dir: str) -> str:
    """
    API function `get_build_script`
      - Usage: Get the build script for a specific project supported in OSS-FUZZ.
      - Return value: The build script for the project.
    """
    global loaded, headerjson
    if not loaded:
        __load_headerfiles()
    
    script = [ "# Begin of build script from headerfiles" ]
    script.append(f"export HEADERFILES_CUSTOM_INSTALL_DIR=\"{install_dir}\"")
    if proj in headerjson:
        script.append(f"mkdir -p {install_dir}/include")
        script.append(f"mkdir -p {install_dir}/lib")
        script.append(f"export CFLAGS=\" -I{install_dir}/include\" ")
        script.append(f"export CXXFLAGS=\" -I{install_dir}/include\" ")
        script.append(f"export LDFLAGS=\" -I{install_dir}/lib\" ")

        script.extend(headerjson[proj].get("build", []))
    script.append("# End of build script from headerfiles")

    return "\n".join(script) + "\n"
