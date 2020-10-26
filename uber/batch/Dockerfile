FROM python:3.7

RUN apt-get update
RUN apt-get install default-jdk -y
RUN apt install libpython2.7-stdlib

# Create app directory
WORKDIR /app

# Install app dependencies
COPY uber_batch/requirement.txt .

RUN pip install -r requirement.txt

# Bundle app source
COPY ga_mobile /app

CMD [ "python", "test.py" ]

