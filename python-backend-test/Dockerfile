FROM python:3
WORKDIR /usr/src/app
RUN pip install --no-cache-dir pipenv && pipenv install
RUN pip install flask
CMD [ "python", "./app.py" ]
