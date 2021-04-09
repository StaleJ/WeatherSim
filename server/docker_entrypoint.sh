#!/bin/bash

set -e

exec python3 -u client_server.py &
exec python3 -u server.py
