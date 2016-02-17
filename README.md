# Mozio Providers API

Full API documentation can be found at: http://docs.mozioapitest.apiary.io/

A Postman collection with all API end points to test locally is available at: https://www.getpostman.com/collections/ba9a4dbc57007120f329

## Local installation
1) Create a directoy where to put the project and you virtual environment
```
mkdir mozio_api_test
cd mozio_api_test
```
2) Create your virtual environment and activate it
```
virtualenv env --no-site-packages
source env/bin/activate
```
3) Clone git repo and install requirements
```
git clone https://github.com/sromero84/mozio_test.git
pip install -r mozio_test/requirements.txt 
```
4) Create your local  `mozio_test` Postgres database. 

5) Run migrations, start the local server and go!

```
cd mozio_test
python manage.py migrate
python manage.py runserver
```

You can go to `http://localhost:8000/api/v1/` to see the available end points.

## Assumptions

It's assumed that a Provider might define a Service Area as multiple geographical areas, that's why the usage of `MultiPolygonField`.

Currency format is defined in ISO_4217 format (https://en.wikipedia.org/wiki/ISO_4217) with a max of 3 characters.

Phone is assumed as international number, without specific format.
