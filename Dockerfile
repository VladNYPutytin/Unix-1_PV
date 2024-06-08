FROM python:3.12.2
WORKDIR /app
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY . /app
RUN mkdir -p data
COPY templates/ templates/
COPY static/ static/
RUN pip install -r requirements.txt
CMD ["python", "main.py"]