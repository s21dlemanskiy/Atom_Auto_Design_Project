# Используем официальный образ Python как базовый
FROM python:3.11.5

# Устанавливаем рабочую директорию в контейнере
WORKDIR ${APP_WORKING_DIR}

# Устанавливаем зависимости
ADD ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы проекта в рабочую директорию
COPY ./app/ .

# Указываем что приложение на 8000 порту (без compose это просто коментарий)
expose ${REST_API_APP_PORT}

# Команда для запуска приложения
ENTRYPOINT uvicorn --host 0.0.0.0 --port ${REST_API_APP_PORT} main:app
