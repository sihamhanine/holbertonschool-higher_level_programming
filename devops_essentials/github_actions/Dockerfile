# Alpine base image 
FROM alpine
# Send message "Hello, World!" when the container runs.
CMD ["echo", "Hello, World! workflow for test"]
# Add the curl package
RUN apk add --no-cache curl
# Add config.txt file to appropriate location
COPY config.txt /app/config.txt