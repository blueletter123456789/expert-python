# ここはビルド用のコンテナ（拡張のビルドが不要ならこちらもslimで可）
FROM python:3.9-buster as builder

WORKDIR /opt/app

COPY requirements.lock /opt/app
RUN pip3 install -r requirements.lock

# ここからは実行用コンテナの準備
FROM python:3.9-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

# もしPostgreSQLとかで必要なOSパッケージがあれば入れる
RUN apt update \
  && apt install -y libpq5 libxml2 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY deploy/uwsgi.ini /opt/app
COPY src /opt/app/src

EXPOSE 8000
CMD ["python", "/opt/app/src/server.py"]