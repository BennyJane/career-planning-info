#!/bin/bash
set -e

echo `service mysql status`

service mysql start
sleep 3
echo `service mysql status`

echo "开始导入数据"
mysql < /mysql/create.sql
sleep 3

tail -f /dev/null


