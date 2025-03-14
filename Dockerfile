FROM python:3.10-slim

WORKDIR /app

COPY generate_fake_products.py /app/
RUN pip install faker requests

CMD ["python3", "/app/generate_fake_products.py"]

