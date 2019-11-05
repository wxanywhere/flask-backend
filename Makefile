.PHONY: clean system-packages python-packages install
.PHONY: database.init database.migrate database.upgrade migrate test run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python-pip -y

python-packages:
	pip install -r requirements.txt

install: system-packages python-packages

database.init:
	python manage.py db init

database.migrate:
	python manage.py db migrate

database.upgrade:
	python manage.py db upgrade

migrate: database.migrate database.upgrade

test:
	ENV=test python manage.py test

run:
	python manage.py run

all: clean install tests run
