# Image de base Alpine
FROM alpine

# Ajouter le package curl
RUN apk add --no-cache curl

# Ajouter le fichier config.txt à l'emplacement approprié
COPY config.txt /app/config.txt

# Spécifier un volume à l'emplacement /data
VOLUME /data

# Envoyer le message "Hello, World!" lorsque le conteneur s'exécute.
CMD ["echo", "Hello, World!"]
