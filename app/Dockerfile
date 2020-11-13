FROM python:3.8-buster
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ADD . /app
#ADD /crawler /app/crawler
#ADD app.py /app
#ADD scrapy.cfg /app
WORKDIR /app
EXPOSE 5000
#ENTRYPOINT ["python3"]
#CMD ["app.py"]