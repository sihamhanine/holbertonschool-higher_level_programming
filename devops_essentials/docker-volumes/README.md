# Docker Volumes - Persistance des Données

## Description

Ce projet démontre l'utilisation des volumes Docker pour persister les données au-delà du cycle de vie des conteneurs.

## Dockerfile

```Dockerfile
# Utiliser l'image de base Alpine
FROM alpine

# Spécifier un volume à /data
VOLUME /data

# Définir la commande par défaut
CMD ["sh"]

Étapes pour Démontrer la Persistance des Données
Construire l'image Docker :

docker build -t my-data-container .

Exécuter un conteneur avec un volume mappé :


docker run -it -v local_data_directory:/data my-data-container

Écrire des données dans le volume :


docker exec -it <container_id> sh -c "echo 'Hello, Docker Volumes!' > /data/hello.txt"

Arrêter le conteneur :


docker stop <container_id>

Redémarrer le conteneur :


docker start <container_id>

Lire les données du volume :


docker exec -it <container_id> sh -c "cat /data/hello.txt"