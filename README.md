# Fred-pilot API


## Installation

### Running a server on your local machine.

#### Deps:

* Python >= 3.8
* Postgres >= 12

#### Steps:
* Clone project

* Install virtualenv using pip3

    `$ pip3 install virtualenv`

* Create virtualenv using python3

    `$ python3 -m virtualenv venv`

* Activate virtualenv

    `$ source venv/bin/activate`

* Run following command and fill all the required setting variables in .env file.

    `$ cp .env.template .env`

* Now install all requirements

    `$ pip3 install -r requirements.txt`

* Setup postgres db and put config in django settings file.

### Running a server

    $ python manage.py runserver
