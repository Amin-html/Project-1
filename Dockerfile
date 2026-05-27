FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY tracbooking .
EXPOSE 8000
CMD ["python", ",amage.py", "runserver", "0.0.0.0:8000"]