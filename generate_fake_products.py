import json
import time
import os
import requests
from faker import Faker

fake = Faker()
ELASTICSEARCH_URL = "http://elasticsearch:9200"
DATA_DIR = "/app/data"  

def wait_for_elasticsearch():
    """ Aguarda o Elasticsearch iniciar antes de continuar. """
    print("Aguardando Elasticsearch iniciar...")
    for _ in range(30):  
        try:
            response = requests.get(ELASTICSEARCH_URL)
            if response.status_code == 200:
                print("Elasticsearch está pronto!")
                return
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(5)
    raise Exception("Erro: Elasticsearch não respondeu a tempo!")

def generate_product():
    """ Gera um produto fake """
    return {
        "name": fake.sentence(nb_words=4),
        "description": fake.text(),
        "category": fake.random_element(["Eletrônicos", "Roupas", "Livros", "Brinquedos", "Casa"]),
        "price": round(fake.random_number(digits=3, fix_len=True) * 1.1, 2),
        "stock": fake.random_int(min=0, max=500)
    }

def generate_bulk_data(filename, num_products=80000):
    """ Gera um arquivo JSON para importação em massa """
    filepath = os.path.join(DATA_DIR, filename)
    os.makedirs(DATA_DIR, exist_ok=True)  # Garante que a pasta exista
    with open(filepath, "w") as f:
        for _ in range(num_products):
            f.write(json.dumps({"index": {"_index": "products"}}) + "\n")
            f.write(json.dumps(generate_product()) + "\n")
    print(f"Arquivo {filepath} gerado com {num_products} produtos!")

def upload_to_elasticsearch(filename):
    """ Envia os produtos para o Elasticsearch """
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "rb") as f:
        response = requests.post(f"{ELASTICSEARCH_URL}/_bulk", headers={"Content-Type": "application/json"}, data=f)
        print(f"Resposta do Elasticsearch: {response.status_code}, {response.text}")

if __name__ == "__main__":
    wait_for_elasticsearch()
    generate_bulk_data("products.json", 80000)
    upload_to_elasticsearch("products.json")
    print("Importação finalizada!")
