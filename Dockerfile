# Use an official Python runtime as a parent image
FROM python:3.10

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"] 

CMD ["manage.py", "runserver", "0.0.0.0:8000"]