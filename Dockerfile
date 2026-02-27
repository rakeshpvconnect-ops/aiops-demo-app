FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
# FIXED: config restored
RUN mkdir -p /etc/app && echo 'version: 1.0.0' > /etc/app/config.yaml
EXPOSE 5000
CMD ["python", "app.py"]
