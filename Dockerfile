FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    LANG=ru_RU.UTF-8

RUN apt-get update && \
    apt upgrade && \
    apt-get install --no-install-recommends -y \
    git \
    gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install deps
COPY ./requirements.txt .
RUN pip install uv && \
    uv pip install --system --no-cache-dir -r requirements.txt

WORKDIR /src
COPY . /src

CMD [ "/src/.dockerinit.sh" ]
EXPOSE 5000
