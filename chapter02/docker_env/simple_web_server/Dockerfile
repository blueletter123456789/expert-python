# ベースイメージを設定
# "python"はオフィシャルなPythonイメージ
# "slim"バージョンは、とりあえずで指定するには軽量で実用的な選択
FROM python:3.9-slim

# イメージをクリーンにするためにワークディレクトリを変更
# "/app/"はこの目的で一般的に利用される
WORKDIR /app/

# ここで静的ファイルをプロジェクトソースツリーから現在のワークディレクトリにコピー
COPY static/ static/

# "python -m http.server"をローカルで実行したいのでエントリーポイントに設定
ENTRYPOINT ["python3", "-m", "http.server"]

# static/ディレクトリのファイルをポート80でデフォルトで提供するため、
# 以下の設定をPythonの組み込みのHTTPサーバーデフォルト引数に設定
CMD ["--directory", "static/", "80"]
