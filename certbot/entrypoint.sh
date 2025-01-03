#!/bin/bash

# 인증서 발급 또는 갱신
# docker-compose.yaml env_file 지정
# env_file에 들어갈 내용
# EMAIL, DOMAIN
certbot certonly -v --webroot --webroot-path=/var/www/html --email ${EMAIL} --agree-tos --no-eff-email -d ${DOMAIN} --non-interactive # --force-renewal

# 권한 수정 안하면 Host에서 안보임
chmod -R 777 /etc/letsencrypt/

# cron 등록 (매분 갱신; 테스트용)
# echo '* * * * * certbot renew --dry-run' > /etc/crontabs/root

# cron 등록 (매주 일요일 00:00에 갱신) "At 00:00 on Sunday."
echo '0 0 * * 0 certbot renew' > /etc/crontabs/root

# crond 실행 # -f 옵션은 foreground로 실행
# daemon으로 실행시 자동 갱신 불가
exec crond -f
