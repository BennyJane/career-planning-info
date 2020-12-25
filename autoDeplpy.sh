#!/bin/bash
#set -ex
set -e

cd `dirname "$0"`
currentPath = `pwd`

echo "[当前目录]： $(pwd)"

webLogPath = $currentPath + '/logs/web'
redisLogPath = $currentPath + '/logs/redis'
gunicornLogPath = $currentPath + '/logs/gunicorn'


function foo() {
  if [ -d webLogPath]
  then
    echo ""
  else
    mkdir webLogPath
  echo "创建日志目录"

}
