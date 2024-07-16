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

# Support List (68 projects till now)

- [x] avahi
- [x] bind9
- [x] bluez
- [x] brotli
- [x] capstone
- [x] coturn
- [x] croaring
- [x] dovecot
- [x] igraph
- [x] inchi
- [x] kamailio
- [x] krb5
- [x] lcms
- [x] libarchive
- [x] libbpf
- [x] libcbor
- [x] libcoap
- [x] libdwarf
- [x] libevent
- [x] libexif
- [x] libfido2
- [x] libfuse
- [x] libgd
- [x] libical
- [x] libjpeg-turbo
- [x] libpcap
- [x] librdkafka
- [x] libredwg
- [x] libressl
- [x] libsndfile
- [x] libsodium
- [x] libsrtp
- [x] libssh
- [x] libssh2
- [x] libtasn1
- [x] libtpms
- [x] libusb
- [x] libvips
- [x] libvnc
- [x] libwebsockets
- [x] libxls
- [x] libyang
- [x] lua
- [x] lwan
- [x] mbedtls
- [x] mdbtools
- [x] minizip
- [x] ndpi
- [x] netcdf
- [x] njs
- [x] oniguruma
- [x] openexr
- [x] opusfile
- [x] ostree
- [x] picotls
- [x] pidgin
- [x] pjsip
- [x] proftpd
- [x] pupnp
- [x] sleuthkit
- [x] tidy-html5
- [x] unicorn
- [x] unit
- [x] utf8proc
- [x] vlc
- [x] w3m
- [x] wasm3
- [x] zydis

# Test

```bash
python3 -m tests.test_api
```
