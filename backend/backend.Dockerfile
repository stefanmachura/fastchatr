FROM python:3.10

RUN apt update && apt upgrade -y
RUN apt install wait-for-it

RUN mkdir -p /opt/app

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh" ]