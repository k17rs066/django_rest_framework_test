# django_rest_framework_test
Django Rest framework を使ってAPIを作ってみる

- 使用環境
  -  python 3.10.1

- 環境構築
  - 使用するライブラリをインストール
    - ```pip install django```
    - ```pip install djangorestframework```

- プロジェクト作成
  - django-admin startproject [プロジェクト名]

- settings.py の INSTALLED_APPS にrest_framework を追加
    ```   
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework' #  この行を追加
        ]
    ```

- django サーバーを動かす
  - ```python manage.py runserver```

- データベース構築
  - マイグレートファイルを作成
    ```
    # migration ファイルを作成する
    python manage.py makemigrations
    ```
    ```
    migration ファイルをもとにDBに反映する
    python manage.py migrate
    ```

- 管理ユーザを作成
  ```
python manage.py createsuperuser 
Username (leave blank to use 'user'): [ユーザ名]
Email address: [メールアドレス]
Password:[パスワード]
Password (again):[再パスワード]
Superuser created successfully.
  ```

- 開発用サーバ立ち上げ
```
    python manage.py runserver
```








