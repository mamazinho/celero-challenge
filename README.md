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
***Why AngularJs?***
* I prefer VueJs to front-end, but angularJs allows a simplicity, because it runs inside Django and not out, as vueJs. The angularJs can be used
as mini-framework better than vue.
***Why the manyToMany relation stay in Athlete_infos and not in Athlete***
* If the relation was been made using the athlete I will open the user and have all events that he goes more easily,
but I would not have the same easily to take his infos for each event. So, it's better that info has many events and
many events with that infos instead athlete. But I open for suggestions about data modeling or another issue.
***Time to run command to populate database***
* I test two ways, the most used to perform a batch is the bulk_create, to make in one query for db, I have tried to follow this way (you can find the code in 'populateDB2.py' file), but the perform gain was very low, because it's slow to read and populate the lists, and it's just a test, I left this file only to example of idea, but not finished. The other way, this works, was make the basic, get_or_create in database (you can find the code in 'populateDB.py'). Both versions can take more than half-hour to run all queries. For this, I left a sql file, if you have no time to waste the better way is make a `mysql celero < challenge/utils/celero.sql` after migrate. I am accepting suggestions of everyone, this was the hardest part for me, make this perform.


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
    $ sudo mysql -e "GRANT ALL ON test_celero.* TO 'celero'@'%' IDENTIFIED BY 'c3l3r0'"

## How to Setup:
    $ workon celc
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py populateDB

## How to Run:
    $ python manage.py runserver

## How to access:
    Your terminal will show an address that looks like 'http://127.0.0.1:[port number]', just put this address in your browser and use it.