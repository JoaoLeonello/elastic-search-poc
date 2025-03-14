# 🚀 Elastic Search PoC

This project demonstrates how to set up an **Elasticsearch + Kibana** environment using Docker, index and store **80,000 fake products**, and query them efficiently.

## **📌 Features**
- ✅ Set up an **Elasticsearch + Kibana** cluster in Docker.
- ✅ Create a `products` index with **optimized mappings**.
- ✅ Generate **80k fake products** automatically using Python (`Faker`).
- ✅ **Bulk upload** the products to Elasticsearch on startup.
- ✅ Expose a **FastAPI-based Swagger API** for testing queries.

---

📌 Getting Started

1️⃣ Clone the repository

git clone this repo

2️⃣ Run the project with Docker
docker compose up -d --build

This will: 
✅ Start Elasticsearch and Kibana in Docker.
✅ Automatically create the products index.
✅ Generate 80,000 fake products and insert them into Elasticsearch.

📌 Testing the API (Swagger)
Once the setup is complete, access:

Elasticsearch: http://localhost:9200 - 
Kibana: http://localhost:5601 - 
Swagger API: http://localhost:8000/docs - 

You can run queries via Swagger UI, such as:

🔍 Search by product name: /search/{name}

🎯 Filter by category: /filter/category/{category}

💰 Filter by price range: /filter/price?min_price=100&max_price=500

📊 Get average price per category: /stats/avg_price_per_category


📌 Next Steps
✅ Optimize index performance with custom analyzers.
✅ Implement pagination for large queries.
⏳ Add real-time updates with event streaming.
