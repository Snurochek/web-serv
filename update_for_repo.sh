#!/bin/bash

cd /home/user/web-serv || exit 1

# Зберігаємо поточний хеш
CURRENT_HASH=$(git rev-parse HEAD)

# Отримуємо останні зміни з репозиторія
git fetch origin

# Якщо є нові коміти — оновлюємо
if [ "$CURRENT_HASH" != "$(git rev-parse origin/main)" ]; then
    echo "Оновлення знайдено. Оновлюємо..."
    git reset --hard origin/main

    # Перезапуск сервера (Flask, systemd, runit, etc.)
    # Якщо runit:
    # sudo sv restart flask-server
    # або якщо systemd:
    sudo systemctl restart flask.service

else
    echo "Немає оновлень."
fi
