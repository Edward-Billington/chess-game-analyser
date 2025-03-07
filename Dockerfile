FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y stockfish && \
    apt-get install -y zstd && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

COPY run.sh /usr/local/bin/analyse
RUN chmod +x /usr/local/bin/analyse
