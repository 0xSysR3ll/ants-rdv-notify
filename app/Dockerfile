FROM python:3-alpine


LABEL maintainer="0xsysr3ll"
LABEL org.label-schema.vendor="0xsysr3ll"
LABEL org.label-schema.url="https://github.com/0xsysr3ll/ants-rdv-notify"
LABEL org.label-schema.name="ants-rdv-notify"
LABEL org.label-schema.description="A French NIC and Passport rendez-vous notifier"
LABEL org.label-schema.usage="https://github.com/0xsysr3ll/ants-rdv-notify"
LABEL org.label-schema.vcs-url="https://github.com/0xsysr3ll/ants-rdv-notify"
LABEL org.label-schema.schema-version="1.0"
LABEL copyright="Copyright © 2023 0xsysr3ll"

WORKDIR /app
COPY . .

RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip install -U pip && \
    pip install -r requirements.txt && \
    apk del .build-deps

CMD ["python", "-u", "main.py"]