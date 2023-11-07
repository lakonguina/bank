#!/bin/bash

# Informations de connexion à la base de données
DB_USER="$POSTGRES_USER"
DB_PASSWORD="$POSTGRES_PASSWORD"
echo $DB_USER

# Répertoire contenant les répertoires des bases de données
BASE_DIR="/usr/src/sql/data/prod/"

# Parcours des répertoires pour chaque base de données
for db_dir in ${BASE_DIR}*; do
    if [ -d "$db_dir" ]; then
        db_name=$(basename "$db_dir")
        echo "Traitement de la base de données : $db_name"

        # Connexion à la base de données correspondante et insertion des fichiers CSV
        for file in "${db_dir}"/*.csv; do
            if [ -f "$file" ]; then
                table_name=$(basename "$file" .csv)

                # Commande d'insertion SQL pour PostgreSQL
                psql --username "$DB_USER" -d "$db_name" -c "\copy $table_name FROM '$file' CSV HEADER"

                if [ $? -eq 0 ]; then
                    echo "Le fichier $file a été inséré dans la table $table_name de la base de données $db_name."
                else
                    echo "Erreur lors de l'insertion du fichier $file dans la table $table_name de la base de données $db_name."
                fi   
            fi
        done
    fi
done
