FROM python:3-alpine

WORKDIR /app
COPY . .

RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip install -U pip && \
    pip install -r requirements.txt && \
    apk del .build-deps

CMD ["python", "-u", "main.py"]