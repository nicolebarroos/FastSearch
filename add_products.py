import random
from app.infrastructure.elasticsearch_client import es  # ✅ Importa conexão já criada

CATEGORIES = ["electronics", "clothing", "sports", "home", "beauty"]
PRODUCT_BASE = ["Smartphone", "Laptop", "Bluetooth Speaker", "Watch", "Mechanical Keyboard"]

def generate_products(qty=10000):
    """Gera produtos fictícios e os insere no Elasticsearch"""
    for i in range(qty):
        product_name = f"{random.choice(PRODUCT_BASE)} {random.randint(1, 10000)}"
        product = {
            "name": product_name,
            "name_suggest": { "input": [product_name] },
            "description": "High-quality product with excellent value.",
            "price": round(random.uniform(50, 5000), 2),
            "category": random.choice(CATEGORIES),
            "image": "https://via.placeholder.com/150"
        }
        es.index(index="products", body=product)  # ✅ Agora es vem do arquivo correto
        print(f"✅ Produto {product_name} indexado!")

if __name__ == "__main__":
    generate_products()