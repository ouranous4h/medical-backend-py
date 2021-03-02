FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /medical-app
WORKDIR /medical-app
COPY requirements.txt /medical-app/
RUN pip install -r requirements.txt
COPY . /medical-app/