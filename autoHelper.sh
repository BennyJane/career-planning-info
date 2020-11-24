#!/bin/bash
set -e

cd `dirname "$0"`
currentPath=`pwd`


dbUp (){
  `flask db migrate`
}

dbInit (){
    `source ./env/Scripts/activate`
  `flask db init`
  `flask db migrate`
  `flask db upgrade`
}

case $1 in
"dbUp" | "dbup")
  dbUp ;;
"dbinit" | "dbInit")
  dbInit ;;
"run")
  `flask run` ;;
 *)
 echo "end";;
esac