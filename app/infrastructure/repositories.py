from elasticsearch import Elasticsearch
from app.domain.interfaces.i_product import ProductRepositoryInterface
from app.domain.entities.product import Product

class ElasticsearchProductRepository(ProductRepositoryInterface):
    """Repositório que interage com o Elasticsearch"""
    
    def __init__(self):
        self.es = Elasticsearch("http://elasticsearch:9200")
        self.index = "products"

    def save(self, product: Product):
        """Salva um produto no Elasticsearch"""
        data = {
            "name": product.name,
            "name_suggest": {  # 🔹 Garante que autocomplete funcione corretamente
                "input": [product.name]
            },
            "description": product.description,
            "price": product.price,
            "category": product.category,
            "image": product.image
        }
        return self.es.index(index=self.index, body=data)

    def search_by_text(self, term: str):
        """Busca produtos por nome ou descrição"""
        query = {
            "bool": {
                "must": [{"multi_match": {"query": term, "fields": ["name", "description"]}}]
            }
        }
        res = self.es.search(index=self.index, body={"query": query}, size=50)
        return [hit["_source"] for hit in res["hits"]["hits"]]

    def autocomplete(self, term: str):
        """Retorna sugestões de produtos"""
        query = {
            "suggest": {
                "product-suggestion": {
                    "prefix": term,
                    "completion": {
                        "field": "name_suggest"
                    }
                }
            }
        }
        res = self.es.search(index=self.index, body=query)
        suggestions = [option["text"] for option in res["suggest"]["product-suggestion"][0]["options"]]
        return suggestions