FROM python:3.11.4-alpine

WORKDIR /app
COPY . .
EXPOSE 8081

CMD ["python", "server.py"]
