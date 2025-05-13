# 🌹 Роза — Telegram WebApp

Готовый Telegram WebApp + Flask backend с деплоем на Render.

## 🔗 Ссылка на деплой

https://rozawebapp.onrender.com/

## ✅ Переменные окружения

- `BOT_TOKEN` — токен Telegram-бота
- `ADMIN_IDS` — список ID админов через запятую
- `WEBAPP_URL` — адрес WebApp

## 🚀 Локальный запуск

```bash
pip install -r requirements.txt
gunicorn wsgi:app
```