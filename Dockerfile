FROM python:3.10

WORKDIR /home

COPY *.txt ./
COPY *env ./ 

RUN pip install -U pip aiogram && apt-get update && pip install -r requirements.txt 

COPY *.py ./

ENTRYPOINT [ "python", "app.py" ]
