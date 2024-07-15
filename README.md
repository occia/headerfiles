# headerfiles
Header file inference tool for LLM-based fuzz driver generation to OSS-Fuzz projects

# API

There are two APIs:

```
headerfiles.api

- is_supported_proj
  - Usage: Check if a projection is supported by the API.
  - Return value: True if the projection is supported, False otherwise.

- get_proj_headers
  - Usage: Get the inferred headers for a specific project.
  - Return value: A list of inferred headers for the project, their orders also matter.

```

# test

```bash
python3 -m tests.test_api
```
