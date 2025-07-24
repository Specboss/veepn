FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    iproute2 \
    iptables \
    qrencode \
    net-tools \
    procps \
    curl \
    gnupg \
    sudo \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN sed -i 's/\r$//g' entrypoint.sh start.sh && chmod +x entrypoint.sh start.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["./start.sh"]
