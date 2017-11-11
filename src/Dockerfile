FROM python:3.6.3
WORKDIR /usr/src/scraper

COPY requirements.txt ./
COPY setup.py ./
COPY Makefile ./
COPY scraper/ ./scraper/.

RUN make init

COPY . .

ENV NAME scraper
