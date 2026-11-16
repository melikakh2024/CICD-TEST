FROM python:3.12-slim
WORKDIR /app
COPY convert.py .
CMD ["python", "convert.py"]
