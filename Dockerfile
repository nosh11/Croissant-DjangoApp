FROM python:alpine

# 作業ディレクトリを設定
WORKDIR /app

# mysqlclientに必要な依存関係をインストール: new
RUN apk add --no-cache pkgconfig python3-dev mariadb-dev build-base



# 依存関係をインストール
RUN pip install --upgrade pip 

# 必要な依存関係をコピーしてインストール
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /code/
RUN pip install gunicorn

# アプリケーションコードとエントリーポイントスクリプトをコピー
COPY . /app/
COPY entrypoint.sh /app/
COPY create_superuser.py /app/

# 実行権限を付与
RUN chmod +x /app/entrypoint.sh

# エントリーポイントスクリプトを設定
COPY entrypoint.sh /code/
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

CMD ["sh", "-c", "python manage.py runserver ${HOST:-0.0.0.0}:${PORT:-8000}"]