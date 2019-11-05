# base image
FROM python:3.7.4

# set working directory
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# add and install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# add app
COPY . .

# run server
CMD python manage.py run -h 0.0.0.0
