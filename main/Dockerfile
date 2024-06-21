# syntax=docker/dockerfile:1

# Definování verze Pythonu pro příkaz FROM.
ARG PYTHON_VERSION=3.11.4

# Nastavení základnéího prostředí pro aplikaci.
FROM python:${PYTHON_VERSION}-slim as base

# Zabraňuje Pythonu zapisovat soubory pyc.
ENV PYTHONDONTWRITEBYTECODE=1

# Udržuje Python od bufferování stdout a stderr.
ENV PYTHONUNBUFFERED=1

# Definice adresáře pro aplikaci v rámci obrazu.
WORKDIR /app

# Vytvoří neprivilegovaného uživatele.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Stáhne závislosti.
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install -r requirements.txt

# Zkopíruje zdrojový kód do kontejneru.
COPY . .

# Exponuje port 8000.
EXPOSE 8000

# Spustí Django aplikaci.
CMD python manage.py runserver 0.0.0.0:8000
