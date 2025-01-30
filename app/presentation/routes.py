from fastapi import APIRouter
from app.application.use_cases.product_use_case import AddProductUseCase, AutocompleteProductUseCase, SearchProdutoUseCase
from app.domain.entities.product import Product

from app.infrastructure.repositories import ElasticsearchProductRepository

router = APIRouter()

repository = ElasticsearchProductRepository()

@router.post("/produtos/")
def add_product(produto: Product):
    """Adiciona um novo produto no Elasticsearch"""
    use_case = AddProductUseCase(repository)
    return use_case.execute(produto)

@router.get("/produtos/busca/")
def search_product(q: str):
    """Busca produtos por nome ou descrição"""
    use_case = SearchProdutoUseCase(repository)
    return use_case.execute(q)

@router.get("/produtos/autocomplete/")
def autocomplete(q: str):
    """Sugere produtos conforme o usuário digita"""
    use_case = AutocompleteProductUseCase(repository)
    return use_case.execute(q)
