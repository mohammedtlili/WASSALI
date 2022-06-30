FROM python:3.10

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

#CMD ["python", "./app/main.py"]
CMD ["uvicorn", "main:fastapi-app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]