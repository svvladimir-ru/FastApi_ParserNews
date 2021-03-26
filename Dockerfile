FROM python:latest

WORKDIR /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
RUN pip install fastapi uvicorn
COPY . /code
EXPOSE 8000
CMD ["python", "main.py"]
