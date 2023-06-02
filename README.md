Для начала работы нужно создать виртуальное окружение и войт в него


`pip install -r requirements.txt` - установка зависимостей


Установка frontend:

`cd diploma-frontend`

`python setup.py sdist`

`pip install ./dist/diploma-frontend-0.6.tar.gz`


Создание бд и загрузка фикстур:

`python manage.py make migrations`

`python manage.py migrate`

`python manage.py loaddata ./fixtures/users.json ./fixtures/profiles.json ./fixtures/products.json ./fixtures/categories.json  ./fixtures/orders.json `

`python manage.py runserver`

Login: 
admin
admin

Customer
Privet123
