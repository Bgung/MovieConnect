FROM certbot/certbot:latest

# bash 설치
RUN apk update && apk add --no-cache bash busybox-suid

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]