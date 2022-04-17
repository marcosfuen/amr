FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -q gunicorn
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /usr/src/app
COPY . .
RUN python manage.py collectstatic --noinput
CMD set -xe; ./run_web.sh; gunicorn gestionEnergetica.wsgi:application --bind 0.0.0.0:8000 --worker-tmp-dir /dev/shm --access-logfile=-
