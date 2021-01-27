This application makes part of Celero's Back-end challenge

Read this Doc in [PT-BR](README.pt.md)

## Technologies
* Django
* Django Rest framework
* AngularJs

## How the project was been build:
* We have a mainly template that will be rendered by django, after load this template, the rest of front-end is render by AngularJS,
where it will start to make requests to the API, which is running with django rest.

## Questions:
***Why use a front-end framework?***
* I chose to use a front-end framework (AngularJs) because it will help so much in interactivity and how the data will be
displayed to user, how the main objective of Django Rest Framework is to be an API (webServices), I treat it like this, leaving the renders
with the front-end and delivering a complete flow.

***Why AngularJs?***
* I prefer VueJs to front-end, but angularJs allows a simplicity, because it runs inside Django and not out, as vueJs. The angularJs can be used
as mini-framework better than vue.

***Why the manyToMany relation stay in Athlete_infos and not in Athlete?***
* If the relation was been made using the athlete I will open the athlete and have all events that he goes more easily,
but I would not have the same easily to take his infos for each event. So, it's better that info has many events and
many events with that infos instead athlete. But I am open for suggestions about data modeling or another issue.

***Time to run command to populate database***
* I test two ways, the most used to perform a batch is the bulk_create, to make in one query for db. I have tried to follow this way (you can find the code in 'populateDB2.py' file), but the perform gain was very low, because it's slow to read and populate the lists, and it's just a test, I left this file only to example of idea, but not finished. The other way, this works, was make the basic, get_or_create (you can find the code in 'populateDB.py'). Both versions can take more than half-hour to run all queries. For this reason I left a sql file, if you have no time to wait all process of populate db, the better way is run the command 
`mysql celero < challenge/utils/athlete_events.sql` after migrate. I am accepting suggestions of everyone, make this have a nice performance was the hardest part for me.

***Why Heroku?***
* Heroku was the best cost benefit that I found, it offer in free plan 10.000 lines in tables on database and has easily intergration with github. It has a delay to make the CRUD operations, sometimes you need refresh the page, this is a problem between angularJs reactivity and Heroku to process this, in local it does not happen.


## Servers:
You can access the application in Heroku App clicking [here](https://challenge-celero.herokuapp.com/).
Heroku has a limit in free plan about quantity of lines in tables on database, for this reason, this version has fewer records of athletes and events. I placed a limit too, for you create new Athletes, Events or Informations for Athletes.

## Run in local machine
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
    or, the fast way to populate:
    $ sudo mysql celero < challenge/utils/celero.sql

## How to Run:
    $ python manage.py runserver

## How to Run Unit Tests:
    $ python manage.py test

## How to access:
    Your terminal will show an address that looks like 'http://127.0.0.1:[port number]', just put this address in your browser and use it.