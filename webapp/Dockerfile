FROM python:3.9.2-alpine

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONPATH /
CMD ["python", "main/api.py"]
