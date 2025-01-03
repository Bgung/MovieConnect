#!/bin/bash

# 인증서 발급 또는 갱신
certbot certonly --webroot --webroot-path=/var/www/certbot --email ${EMAIL} --agree-tos --no-eff-email -d ${DOMAIN} --non-interactive

# cron 등록 (매분 갱신; 테스트용)
# echo '* * * * * certbot renew --dry-run' > /etc/crontabs/root

# cron 등록 (매주 일요일 00:00에 갱신) "At 00:00 on Sunday."
echo '0 0 * * 0 certbot renew' > /etc/crontabs/root

# crond 실행 # -f 옵션은 foreground로 실행
exec crond -f
