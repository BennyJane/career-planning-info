#!/bin/bash
set -e

cd $(dirname "$0")
echo "[当前目录]： $(pwd)"

startApp () {
  flask db upgrade
  sleep 4
  gunicorn -c gunicorn.conf.py application:app --preload
}

run () {
  case $1 in
  "")
    startApp
    ;;
  *)
    echo "end..."
    ;;
  esac
}

run
