FROM python:3.9

RUN pip install pipenv
ADD ./Pipfile .
ADD ./Pipfile.lock .
RUN pipenv install --system --deploy

ADD ./app /app/app
COPY ./manage.py /app
WORKDIR /app
CMD uvicorn --uds /socks/auth-service.sock --log-level debug app.main:app
