import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import headerfiles.api as api

def test_is_supported_proj():
    assert api.is_supported_proj("libfdk-aac")
    assert api.is_supported_proj("libfuse")
    assert api.is_supported_proj("libpsl")
    assert api.is_supported_proj("libsodium")
    assert api.is_supported_proj("libtasn1")
    assert api.is_supported_proj("libyal")
    assert not api.is_supported_proj("aaa")

def check_result_is_list_of_strings(result):
    assert isinstance(result, list)
    assert len(result) == 0 or all(isinstance(x, str) for x in result)

def test_get_proj_headers():
    check_result_is_list_of_strings(api.get_proj_headers("libfdk-aac"))
    check_result_is_list_of_strings(api.get_proj_headers("libfuse"))
    check_result_is_list_of_strings(api.get_proj_headers("libpsl"))
    check_result_is_list_of_strings(api.get_proj_headers("libsodium"))
    check_result_is_list_of_strings(api.get_proj_headers("libtasn1"))
    check_result_is_list_of_strings(api.get_proj_headers("libyal"))
    assert api.get_proj_headers("aaa") is None

if __name__ == "__main__":
    test_is_supported_proj()
    test_get_proj_headers()
    print("All tests passed!")
