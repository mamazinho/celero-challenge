This application makes part of Celero's challenge


## Technologies
* Django
* Django Rest framework
* AngularJs

## How the project was been build:
* We have a mainly template that will be rendered by django, after load this template, the rest of front-end is render by AngularJS,
where it will start to make requests to the API, which is running with django rest.

## Questions:
***Why use a front-end framework?***
* I opt for use a front-end framework (AngularJs) because it will help so much in interactivity and how the data will be
displayed to user, how the main objective of Django Rest Framework is to be an API (webServices), I treat it like this, leaving the renders
with the front-end and delivering a complete flow.
***Why the manyToMany relation stay in Athlete_infos and not in Athlete***
* If the relation was been made using the athlete I will open the user and have all events that he goes more easily,
but I would not have the same easily to take his infos for each event. So, it's better that info has many events and
many events with that infos instead athlete. But I open for suggestions about data modeling or another issue.


You can find how make your setup and run the project in your Linux machine in the text below:

## Install virtualenvwrapper and create a virtualenv:
    $ sudo apt-get install python-pip
    $ pip install --upgrade virtualenv
    $ sudo apt-get install python3 python3-pip virtualenvwrapper libmysqlclient-dev libsnappy-dev gcc libssl-dev
    $ source /etc/bash_completion.d/virtualenvwrapper
    $ mkvirtualenv -p /usr/bin/python3 celc

## How to create DB:
    $ sudo apt install mysql-server
    $ sudo mysql -e "CREATE DATABASE celero"
    $ sudo mysql -e "CREATE USER celero IDENTIFIED BY 'c3l3r0'"
    $ sudo mysql -e "GRANT ALL ON celero.* TO 'celero'@'%' IDENTIFIED BY 'c3l3r0'"

## How to Setup:
    $ workon celc
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py populateDB

## How to Run:
    $ python manage.py runserver

## How to access:
    Your terminal will show an address that looks like 'http://127.0.0.1:[port number]', just put this address in your browser and use it.