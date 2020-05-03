# work-at-olist


Application available in Heroku: [Olist At Work - Heroku](https://olistproject.herokuapp.com/)

[![Build Status](https://travis-ci.com/jona04/work-at-olist.svg?branch=master)](https://travis-ci.com/jona04/work-at-olist)
[![codecov](https://codecov.io/gh/jona04/work-at-olist/branch/master/graph/badge.svg)](https://codecov.io/gh/jona04/work-at-olist)
[![Updates](https://pyup.io/repos/github/jona04/work-at-olist/shield.svg)](https://pyup.io/repos/github/jona04/work-at-olist/)
[![Python 3](https://pyup.io/repos/github/jona04/work-at-olist/python-3-shield.svg)](https://pyup.io/repos/github/jona04/work-at-olist/)


To install need to use Pipenv

Then open the console and write:
```console
pipenv install --dev
```

### Configuring the database

Two ways of create a database: first with Sqlite and second with Postgres:

* Sqlite - Comment the tag DATABASE_URL inside of contrib/env-sample

* Postgres - Just follows the steps in the tag DATABASE_URL inside of contrib/env-sample

The migrations already is automatic in heroku

### Travis

Travis was configurated to make the follow test before deploy:

```
  - pipenv run flake8
  - pipenv run pytest --cov=olist
```

### Tests

The pytest is not completed yet

### API 

To build the api was used the Dango Rest Frame Work

Still in development

### Access Dajngo Admin

To check the Django Admin in Heroku web site was created an user teste.

To entry access the [Olist At Work - Admin Heroku](https://olistproject.herokuapp.com/admin)

Then use:
* username: teste
* password: teste12345

The user have access to view the models.

