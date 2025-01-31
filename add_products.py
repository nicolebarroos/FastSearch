import random
from app.infrastructure.elasticsearch_client import es

CATEGORIES = [
    "eletrônicos", "vestuário", "esportes", "casa e decoração", "beleza e saúde", "livros", 
    "automotivo", "brinquedos", "alimentos", "bebidas", "móveis", "ferramentas"
]

PRODUCT_BASE = [
    "Celular", "Notebook", "Fone de Ouvido Bluetooth", "Televisão", "Teclado Mecânico", 
    "Geladeira", "Fogão", "Micro-ondas", "Liquidificador", "Aspirador de Pó", "Ventilador", 
    "Tênis de Corrida", "Chuteira", "Bicicleta", "Bola de Futebol", "Relógio Smartwatch", 
    "Perfume", "Shampoo", "Maquiagem", "Protetor Solar", "Livro de Romance", "Livro de Ficção", 
    "Livro Técnico", "Brinquedo Educativo", "Carrinho de Bebê", "Cadeira Gamer", "Escrivaninha",
    "Guarda-roupa", "Furadeira", "Serra Elétrica", "Cerveja Artesanal", "Vinho Tinto", 
    "Café Especial", "Chocolate", "Arroz", "Feijão", "Macarrão"
]

def generate_products(qty=10000):
    """Gera produtos fictícios brasileiros e os insere no Elasticsearch"""
    for i in range(qty):
        product_name = f"{random.choice(PRODUCT_BASE)} {random.randint(1, 10000)}"
        product = {
            "name": product_name,
            "name_suggest": { "input": [product_name] },
            "description": "Produto de alta qualidade e ótimo custo-benefício.",
            "price": round(random.uniform(10, 10000), 2),
            "category": random.choice(CATEGORIES),
            "image": "https://via.placeholder.com/150"
        }
        es.index(index="products", body=product)
        print(f"✅ Produtoo {product_name} indexado!")

if __name__ == "__main__":
    generate_products()
