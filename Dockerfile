FROM python

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD api/ api
ADD shittytrello/ shittytrello
ADD manage.py .

ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
