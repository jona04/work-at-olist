# work-at-olist


Application available in Heroku: [Olist At Work - Heroku](https://olistproject.herokuapp.com/)

[![Build Status](https://travis-ci.com/jona04/work-at-olist.svg?branch=master)](https://travis-ci.com/jona04/work-at-olist)
[![codecov](https://codecov.io/gh/jona04/work-at-olist/branch/master/graph/badge.svg)](https://codecov.io/gh/jona04/work-at-olist)
[![Updates](https://pyup.io/repos/github/jona04/work-at-olist/shield.svg)](https://pyup.io/repos/github/jona04/work-at-olist/)
[![Python 3](https://pyup.io/repos/github/jona04/work-at-olist/python-3-shield.svg)](https://pyup.io/repos/github/jona04/work-at-olist/)


To install need to use Pipenv

Then, to install all the package requirements, execute the code in console, inside the project folder:
```console
pipenv install --dev
```

### Configuring the database

Two ways of create a database: first with Sqlite and second with Postgres:

* Sqlite - Not use tag DATABASE_URL inside of contrib/env-sample;

* Postgres - Just follows the steps in the tag DATABASE_URL inside of contrib/env-sample.

### File .env

In contrib/env-sample there is an example of all the environment variables used in the project. 
To do this was used the library [python-decouple](https://github.com/henriquebastos/python-decouple).

The variables who are empty, is not obligatory.  

The variables who have AWS in the name, need your own credentials. This is needed to deploy the static files in AWS S3. 
More about it in the next section.

### Collect Static Files

In the env-sample file there is three variables:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_STORAGE_BUCKET_NAME

This variables are used to configurate the collect static in Heroku. The first two variables is referent of User IAM. 
The third variable is the name of your bucket.

To create the static files you need to run the follow code in console:

```
python manage.py collectstatic
```

### Travis

The Travis was configurated to make the follow tests before deploy:

```
  - pipenv run flake8
  - pipenv run pytest --cov=olist
```

### Tests

The pytest is not completed yet.

### API 

To build the api was used the [Dango REST frameWork](https://www.django-rest-framework.org).

And you can access directly by the Heroku url home of this Project.

```
https://olistproject.herokuapp.com/
```

### Access Django Admin

To check the Django Admin in Heroku, was created an user *teste*.

Access the site [Olist At Work - Admin Heroku](https://olistproject.herokuapp.com/admin) and use the follow pass:

* username: teste
* password: teste12345

The user have access just to view the models.

### Populating Author with CSV file

This feature is in progress.

### CRUD - API

The ModelViewSet in Django REST framework already implements actions for GET, POST, PUT and DELETE HTTP methods.

```
base_url = https://olistproject.herokuapp.com/
```

To list all models, set the follow HTTP request:

```
GET base_url/authors/
GET base_url/books/
```

To Create an model:

```
POST base_url/books/

{
 "name": // Name of the book;
 "edition": // Edition number;
 "publication_year": // Publication year of the book;
 "authors": [] // List of author ids, same ids of previous imported data
}

POST base_url/authors/

{
 "name": // Name of the author;
}
```

To Update an model:

```
PUT base_url/books/{id}/

{
 "name": // Name of the book;
 "edition": // Edition number;
 "publication_year": // Publication year of the book;
 "authors_id": [] // List of author ids, same ids of previous imported data
}

PUT base_url/authors/{id}/

{
 "name": // Name of the author;
}
```

To Delete an model:

```
DELETE base_url/books/{id}/
DELETE base_url/authors/{id}/
```

Note: The relationship among the models are PROTECTED. So to delete some models, you need to edit the Book and remove the Author. Then you can DELETE the specific book or author.