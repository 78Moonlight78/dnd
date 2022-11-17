FROM python:3.10-bullseye
ADD server.py /server/

WORKDIR /server/
RUN pip install redis

CMD [ "python3", "./server.py" ]