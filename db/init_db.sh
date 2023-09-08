#!/bin/bash
set -e

echo "Starting database deployment"

echo "Creating tables"
mysql -u"root" -p"$MYSQL_ROOT_PASSWORD" "$MYSQL_DATABASE" < ../db_scripts/create_tables.sql

echo "Successfully created tables"
echo "Creating functions"
cd ../db_scripts/Functions
for file in * 
    do 
    echo "$file"
    mysql -u"root" -p"$MYSQL_ROOT_PASSWORD" "$MYSQL_DATABASE" < "$file"
done
echo "Successfully created functions"

echo "Creating procedures"

cd ../Procedures/Matches
for file in * 
    do 
    echo "$file"
    mysql -u"root" -p"$MYSQL_ROOT_PASSWORD" "$MYSQL_DATABASE" < "$file"
done

cd ../Players
for file in * 
    do 
    echo "$file"
    mysql -u"root" -p"$MYSQL_ROOT_PASSWORD" "$MYSQL_DATABASE" < "$file"
done

cd ../Teams
for file in * 
    do 
    echo "$file"
    mysql -u"root" -p"$MYSQL_ROOT_PASSWORD" "$MYSQL_DATABASE" < "$file"
done

cd ../Tournaments
for file in * 
    do 
    echo "$file"
    mysql -u"root" -p"$MYSQL_ROOT_PASSWORD" "$MYSQL_DATABASE" < "$file"
done
echo "Successfully created procedures"
echo "Successfully finished database deployment"