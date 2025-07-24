#!/bin/sh

# Проверка наличия скрипта wait-for-it.sh. Если нет, скачать его
if [ ! -f "./wait-for-it.sh" ]; then
  echo "Скрипт wait-for-it.sh не найден. Скачиваем..."
  curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
  chmod +x wait-for-it.sh
fi

./wait-for-it.sh db:5432 -- echo "База данных доступна!"

exec "$@"
