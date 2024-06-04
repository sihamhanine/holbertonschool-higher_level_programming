# Alpine base image 
FROM alpine
# Send message "Hello, World!" when the containers runs.
CMD ["echo", "Hello, World!"]
# Add the curl package
RUN apk add --no-cache curl
# Add config.txt file to appropriate location
COPY config.txt /app/config.txt