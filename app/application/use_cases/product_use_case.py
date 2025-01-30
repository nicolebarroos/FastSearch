

from app.domain.entities.product import Product
from app.domain.interfaces.i_product import ProductRepositoryInterface


class AddProductUseCase:
    """Caso de uso para adicionar produtos"""
    
    def __init__(self, repository: ProductRepositoryInterface):
        self.repository = repository

    def execute(self, product: Product):
        return self.repository.save(product)

class SearchProdutoUseCase:
    """Caso de uso para busca full-text"""
    
    def __init__(self, repository: ProductRepositoryInterface):
        self.repository = repository

    def execute(self, term: str):
        return self.repository.search_by_text(term)

class AutocompleteProductUseCase:
    """Caso de uso para autocomplete"""
    
    def __init__(self, repository: ProductRepositoryInterface):
        self.repository = repository

    def execute(self, term: str):
        return self.repository.autocomplete(term)
