FROM python:3.10-alpine
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
