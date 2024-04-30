#!/bin/sh
until python manage.py migrate; do
  sleep 2
  echo "Retry!";
done
python manage.py compilemessages
python manage.py collectstatic --noinput --clear
echo "Django is ready.";
gunicorn --log-level debug --bind :80 config.wsgi:application --forwarded-allow-ips="*" --timeout 600