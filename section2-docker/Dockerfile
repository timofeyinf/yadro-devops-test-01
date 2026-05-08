FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY http_client.py .

CMD ["python3", "http_client.py"]
