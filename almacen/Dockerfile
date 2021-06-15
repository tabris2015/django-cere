# imagen base
FROM python:3
# variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
# directorio de trabajo
WORKDIR /app
# instalar dependencias
RUN pip install django django-extensions psycopg2
# copiar el codigo fuente
COPY . /app/
