# Veepn

## Стек

- Python 3.12  
- Django + Django REST Framework  
- Redis + Celery  
- **Хранилище файлов:** MinIO   
- **ASGI сервер:** Gunicorn

## Деплой

### Локальный запуск

```bash
git clone https://github.com/Specboss/veepn.git
cd veepn
cp .env_example .env
sudo docker compose -f local.yml up -d --build
```

### Продакшн запуск

```bash
git clone https://github.com/Specboss/veepn.git
cd veepn
cp .env_example .env
sudo docker compose -f prod.yml up -d --build
```