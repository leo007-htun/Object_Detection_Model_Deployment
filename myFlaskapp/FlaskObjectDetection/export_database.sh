#!/bin/sh
#bash ___ .sh
#mysqldump -u [username] -p [database name] > [database name].sql

echo "Enter username of the database : "
echo "Default database name : obj_det "
read usr
echo "Enter the name of the original/created database : "
read name1
echo "Enter the new database name to export in '.sql': "
read name2
sudo mysqldump -u $usr -p $name1 > $name2.sql