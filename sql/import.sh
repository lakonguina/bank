#!/bin/bash

# Credentials
DB_USER="$POSTGRES_USER"
DB_PASSWORD="$POSTGRES_PASSWORD"

# Path containing datas 
BASE_DIR="/usr/src/sql/data/prod/"

for db_dir in ${BASE_DIR}*; do
    if [ -d "$db_dir" ]; then

        db_name=$(basename "$db_dir")
        echo "Treating: $db_name"

        # Connected to the corresponding database and insert file
        for file in "${db_dir}"/*.csv; do
            if [ -f "$file" ]; then
                table_name=$(basename "$file" .csv)

                # Commande to insert into PostgreSQL
                psql --username "$DB_USER" -d "$db_name" -c "\copy $table_name FROM '$file' CSV HEADER"

                if [ $? -eq 0 ]; then
                    echo "$file has been inserted into $db_name.$table_name"
                else
                    echo "Erreur while inserting file $file  in $db_name.$table_name"
                fi   
            fi
        done
    fi
done

# Path containing datas 
BASE_DIR="/usr/src/sql/data/dev/frontoffice/"

FILE_ORDER_FRONTOFFICE=("users" "emails" "phones")

for f in "${FILE_ORDER_FRONTOFFICE[@]}"; do
    psql --username "$DB_USER" -d "$db_name" -c "\copy $f FROM '$BASE_DIR$f.csv' CSV HEADER"

	if [ $? -eq 0 ]; then
		echo "$BASE_DIR$f.csv has been inserted into $db_name.$f"
	else
		echo "Erreur while inserting file $BASE_DIR$f.csv in $db_name.$f"
	fi   
done
