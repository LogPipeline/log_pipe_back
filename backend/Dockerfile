FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend/

RUN apt-get update && apt-get -y install libpq-dev
RUN apt-get install -y netcat

COPY entrypoint.sh /usr/src/local/entrypoint.sh
COPY requirements.txt /backend/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /backend/

RUN ["chmod", "+x", "/usr/src/local/entrypoint.sh"]

