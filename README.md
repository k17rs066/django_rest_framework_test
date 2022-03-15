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
  - ```INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework' #  この行を追加]```

- 




