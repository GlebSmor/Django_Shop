mk venv
pip install -r requirements.txt 

cd diploma-frontend
python setup.py sdist
pip install ./dist/diploma-frontend-0.6.tar.gz

python manage.py make migrations
python manage.py migrate
python manage.py loaddata ./fixtures/users.json ./fixtures/profiles.json ./fixtures/products.json ./fixtures/categories.json  ./fixtures/orders.json 
python manage.py runserver

Login: 
admin
admin

Customer
Privet123