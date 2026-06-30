FROM nginx:alpine

RUN mkdir -p /nginx-cache/

ARG GITHUB_SHA
RUN mkdir -p /var/www && echo "$GITHUB_SHA" > /var/www/commit_id.txt

COPY nginx.conf /etc/nginx/nginx.conf
