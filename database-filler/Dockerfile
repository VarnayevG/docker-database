FROM python:3.8

ARG DATA_PATH   
ENV DATA_PATH ${DATA_PATH}

WORKDIR usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir 
COPY ./fill_db.py ./

CMD python3 -u fill_db.py $DATA_PATH