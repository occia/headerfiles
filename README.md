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

# Support List

- [] bitcoin-core
- [] bluez
- [] brpc
- [] geos
- [] gnutls
- [] hostap
- [] ibmswtpm2
- [] igraph
- [] knot-dns
- [] krb5
- [x] libfdk-aac
- [x] libfuse
- [x] libpsl
- [x] libsodium
- [] libtasn1
- [] libyal
- [] mdbtools
- [] mosh
- [] njs
- [] opendnp3
- [] openexr
- [] pcre2
- [] piex
- [] proj4
- [] protobuf-c
- [] quickjs
- [] resiprocate
- [] rnp
- [] spirv-tools
- [] util-linux
- [] varnish
- [] wget
- [] wget2
- [] xs
- [] znc

# test

```bash
python3 -m tests.test_api
```
