# venv起動と終了
```
 cd bin
 # venv仮想環境に入る
 source activate
 # venv 終了
 deactivate
 # django起動
 python manage.py runserver <portNo>
```

# 環境構築
## pip でdjango をインストール
```
pip install -r requirements.txt
```

## データベース作成
```
# postgre Start
postgres -D /usr/local/var/postgres
# データベース作成
createdb private_diary
# データベース確認
psql -l
# ドライバのインストール psycopg2
pip install -r requirements.txt
```

## Djangoプロジェクトの作成
```
django-admin startproject private_diary
```

## Djangoアプリケーションの作成
```
python manage.py startapp diary
```

## settings.pyの言語とタイムゾーンを日本語にする
```
LANGUAGE_CODE= 'ja'
TIME_ZONE = 'Asia/Tokyo'
```

## Djangoのデータベース設定をPostgreSQLに変更
settings.pyのDATABASES参照

## ロギングの設定
settings.pyのLOGGING参照

## ルーティングの設定
urls.py参照

# vscode設定
## flake8の設定
https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb

# 認証用アプリケーション作成
```
python manage.py startapp accounts
python manage.py makemigrations
python manage.py migrate
```
