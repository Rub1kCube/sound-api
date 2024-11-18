FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    LANG=ru_RU.UTF-8

RUN apt-get update && \
    apt upgrade && \
    apt install git -y && \
    apt-get clean &&  \
    rm -rf /var/lib/apt/lists/*

WORKDIR /src
COPY . /src

# Install deps
RUN pip install uv && uv pip install --system --no-cache-dir -r pyproject.toml --all-extras

CMD [ "/src/.dockerinit.sh" ]
EXPOSE 5000
