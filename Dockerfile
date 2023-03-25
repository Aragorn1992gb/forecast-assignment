FROM python:3

WORKDIR '/app'

RUN apt-get update
RUN apt-get install libpq-dev -y

RUN apt-get install net-tools
RUN apt-get install vim -y

COPY requirements.txt ./

RUN pip3 install -r requirements.txt
RUN pip install python-dotenv

COPY . .

ENV FLASK_APP=main.py
# ENV GOOGLE_APPLICATION_CREDENTIALS=credentials_dev.json
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]