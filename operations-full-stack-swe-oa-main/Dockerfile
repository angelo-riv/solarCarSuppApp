# Docker file for the api

FROM python:3.11-slim

ADD main.py .

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]