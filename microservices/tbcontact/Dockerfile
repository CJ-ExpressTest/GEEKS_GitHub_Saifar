FROM python:3.12-slim

 
RUN apt-get update
RUN apt-get install -y wget cron



WORKDIR /tbcontact_cronjob

ADD . /tbcontact_cronjob

COPY crontab /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab

RUN pip install --no-cache-dir -r requirements.txt

CMD cron && fastapi run main.py --port 80
