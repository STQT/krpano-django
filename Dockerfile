FROM python:3.10

RUN apt-get update && apt-get install -y gettext libgettextpo-dev libproj-dev gdal-bin python3-gdal
RUN mkdir /backend
WORKDIR /backend
ADD requirements.txt /backend/

RUN pip install -r requirements.txt
ADD . /backend/
EXPOSE 8000
RUN chmod +x entrypoint.sh
CMD ["sh", "/backend/entrypoint.sh"]
