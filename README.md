Django アプリケーション
# 環境の前提
 - OS : mac
 - python: 3.7.3
    - venvを利用
 - Django: 3
 - DB: postgre ローカルにインストール
    postgreのドライバとしてpsycopg2を利用

# 初期構築
## 前提
 - python, postgreはインストール済み

## 手順
### ソースコード取得
```bash:
git clone git@github.com:agotoh/venv_private_diary.git
```
### データベース作成
```bash:
# postgre Start
postgres -D /usr/local/var/postgres
# データベース作成
createdb private_diary
# データベース確認
psql -l
```
# 運用コマンド
## venv仮想環境に入る
```bash:
cd bin
# venv仮想環境に入る
source activate
# venv 終了
deactivate
```
## djangoの起動
```bash:
python manage.py runserver --settings private_diary.settings.settings_dev
```
## pip install
requirements.txtに追加の上
```
pip install -r requirements.txt
```

## migration
```
# migration ファイル作成
python manage.py makemigrations --settings private_diary.settings.settings_dev
python manage.py migrate --settings private_diary.settings.settings_dev
```

## スーパーユーザの作成
```
python manage.py createsuperuser --settings private_diary.settings.settings_dev
```
user_name:admin
email: admin@example.com
password: admin135

## Djangoコマンドを使ってpostgreSQLにログインする方法
```
python manage.py dbshell  --settings private_diary.settings.settings_dev
\dt
select * from diary_diary;
```


