#!/bin/bash
cd /home/user/documents/web-server || exit

# Запам’ятай хеш поточного коміту
OLD_COMMIT=$(git rev-parse HEAD)

# Оновлення з репозиторія
git pull origin main

# Якщо коміт оновився — перезапусти сервер
NEW_COMMIT=$(git rev-parse HEAD)

if [ "$OLD_COMMIT" != "$NEW_COMMIT" ]; then
  echo "$(date): Updated. Restarting server..."
  systemctl restart flask-remote
else
  echo "$(date): No changes."
fi
