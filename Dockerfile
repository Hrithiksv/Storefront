FROM python:3.11.3-slim-buster

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy

WORKDIR /app
COPY . /app

RUN pip install pipenv
RUN pipenv install

EXPOSE 8000

CMD [ "python", "manage.py","runserver"]










