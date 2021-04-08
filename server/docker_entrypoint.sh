#!/bin/bash

set -e

exec python3 server.py &
exec python3 client_server.py
