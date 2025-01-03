FROM certbot/certbot:latest

RUN apk update && apk add --no-cache bash busybox-suid

RUN mkdir -p /etc/letsencrypt && \
    chmod 755 /etc/letsencrypt && \
    mkdir -p /var/log/letsencrypt && \
    chmod 755 /var/log/letsencrypt && \
    mkdir -p /var/www/certbot && \
    chmod 755 /var/www/certbot

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]