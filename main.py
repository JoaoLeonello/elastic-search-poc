from fastapi import FastAPI
import requests

app = FastAPI()

ELASTICSEARCH_URL = "http://elasticsearch:9200/products/_search"

@app.get("/search/{name}")
def search_by_name(name: str):
    query = {"query": {"match": {"name": name}}}
    response = requests.get(ELASTICSEARCH_URL, json=query)
    return response.json()

@app.get("/filter/category/{category}")
def search_by_category(category: str):
    query = {"query": {"term": {"category": category}}}
    response = requests.get(ELASTICSEARCH_URL, json=query)
    return response.json()

@app.get("/filter/price")
def search_by_price_range(min_price: float, max_price: float):
    query = {"query": {"range": {"price": {"gte": min_price, "lte": max_price}}}}
    response = requests.get(ELASTICSEARCH_URL, json=query)
    return response.json()
