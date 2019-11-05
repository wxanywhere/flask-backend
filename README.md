# README

Setup environment:  </br>
  `brew install pipenv` </br>
  `pipenv install` </br>
  `pipenv shell`

Init DB:  </br>
  `make database.init`  </br>
  `make database.migrate`

Test:
  `make test`

Run app:
  `make run`
  `python manage.py run`
  `python manage.py run --host 0.0.0.0 --port 5001`
  `python -m pdb  manage.py run --host 0.0.0.0 --port 5001`

Reference:
  `https://github.com/khaile/flask-restplus`
  `https://github.com/cosmic-byte/flask-restplus-boilerplate`
  `https://github.com/Shulyakovskiy/flask-restplus-template`
  `https://github.com/Shulyakovskiy/flask-restplus-jwtext`
  `https://github.com/ramAdam/betty`
