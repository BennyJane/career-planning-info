#!/bin/bash
#set -ex
set -e

cd $(dirname "$0")
currentPath=$(pwd)

echo "[当前目录]： $(pwd)"

$(flask db upgrade)
sleep 4
$(gunicorn -c gunicorn.conf.py application:app --preload)
