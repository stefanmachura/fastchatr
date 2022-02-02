FROM python:3.10

RUN mkdir -p /opt/app

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN alembic upgrade head

CMD ["uvicorn", "app.main:app", "--reload", "--host=0.0.0.0"]%   