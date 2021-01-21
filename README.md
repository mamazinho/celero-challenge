This application makes part of Celero's challenge, it solves both challenges, back-end and front-end

## Technologies
* Django
* Django Rest framework
* AngularJs

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