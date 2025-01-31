from fastapi import APIRouter
from app.application.use_cases.product_use_case import AddProductUseCase, AutocompleteProductUseCase, SearchProdutoUseCase
from app.domain.entities.product import Product
from app.infrastructure.repositories import ElasticsearchProductRepository
from elasticsearch import Elasticsearch

router = APIRouter()

es = Elasticsearch("http://elasticsearch:9200")

repository = ElasticsearchProductRepository()

@router.post("/produtos/")
def add_product(produto: Product):
    """Adiciona um novo produto no Elasticsearch"""
    use_case = AddProductUseCase(repository)
    return use_case.execute(produto)

@router.get("/produtos/busca/")
def search_products(q: str):
    """Busca produtos pelo nome ou descrição"""
    use_case = SearchProdutoUseCase(repository)
    return {"products": use_case.execute(q)}

@router.get("/produtos/autocomplete/")
def autocomplete(q: str):
    """Sugestões de autocomplete para produtos"""
    use_case = AutocompleteProductUseCase(repository)
    return {"suggestions": use_case.execute(q)}