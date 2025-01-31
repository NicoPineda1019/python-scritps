FROM python:3.11

COPY . .
RUN pip3 install --cache-dir=/home/ec2-user/pip_cache -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

CMD [ "python3", "./test.py" ]
