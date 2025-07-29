# SubHub API

## Стек

- Python 3.12  
- Django + Django REST Framework  
- Redis + Celery  
- **Хранилище файлов:** MinIO   
- **ASGI сервер:** Gunicorn
- **Метрики и мониторинг:** Prometheus + Grafana

## Деплой

### Локальный запуск

```bash
git clone https://github.com/Specboss/subhub-api.git
cd subhub-api
cp .env_example .env
sudo docker compose -f local.yml up -d --build
```

### Продакшн запуск

```bash
git clone https://github.com/Specboss/subhub-api.git
cd subhub-api
cp .env_example .env
sudo docker compose -f prod.yml up -d --build
```