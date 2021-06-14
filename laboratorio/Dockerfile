FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN ls
RUN apt update
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
