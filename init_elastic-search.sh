#!/bin/bash

echo "Esperando o Elasticsearch iniciar..."
until curl -s http://localhost:9200 >/dev/null; do
  sleep 5
done

echo "Criando índice products..."
curl -X PUT "localhost:9200/products" -H "Content-Type: application/json" -d '{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  },
  "mappings": {
    "properties": {
      "name": { "type": "text" },
      "description": { "type": "text" },
      "category": { "type": "keyword" },
      "price": { "type": "float" },
      "stock": { "type": "integer" }
    }
  }
}'

echo "Índice criado com sucesso!"
