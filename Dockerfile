FROM nginx:alpine

RUN mkdir -p /nginx-cache/

COPY nginx.conf /etc/nginx/nginx.conf
