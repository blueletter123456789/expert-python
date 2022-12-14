FROM python:3.9-slim

WORKDIR /app/

COPY static/ static/

ENTRYPOINT ["python3", "-m", "http.server"]

CMD ["--directory", "static/", "80"]
