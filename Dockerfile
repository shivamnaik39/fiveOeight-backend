FROM node:18.16.0-alpine3.18 AS build

WORKDIR /app

COPY /frontend/package.json .

RUN npm install

COPY /frontend .

RUN npm run build
# ____________________________________

FROM python:3.10

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY /backend/requirements.txt .

RUN pip install -r requirements.txt

COPY /backend .

COPY certificates/ZscalerRootCertificate-2048-SHA256.crt /usr/local/share/ca-certificates

RUN  update-ca-certificates

COPY --from=build /app/build .

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]