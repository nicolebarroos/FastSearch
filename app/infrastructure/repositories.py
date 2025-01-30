from app.domain.entities.product import Product
from app.domain.interfaces.i_product import ProductRepositoryInterface
from app.infrastructure.elasticsearch import es

class ElasticsearchProductRepository(ProductRepositoryInterface):
    """Implementação do repositório usando Elasticsearch"""

    def save(self, produto: Product):
        doc = produto.dict()
        res = es.index(index="products", body=doc)
        return {"message": "Produto adicionado!", "id": res["_id"]}

    def search_by_text(self, term: str):
        query = {
            "query": {
                "multi_match": {
                    "query": term,
                    "fields": ["name", "description"]
                }
            }
        }
        res = es.search(index="products", body=query)
        products = [hit["_source"] for hit in res["hits"]["hits"]]
        return {"products": products}

    def autocomplete(self, term: str):
        query = {
            "query": {
                "match_phrase_prefix": {
                    "name": term
                }
            }
        }
        res = es.search(index="products", body=query)
        suggestions = [hit["_source"]["name"] for hit in res["hits"]["hits"]]
        return {"sugestoes": suggestions}
