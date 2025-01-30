from abc import ABC, abstractmethod

from app.domain.entities.product import Product

class ProductRepositoryInterface(ABC):
    """Interface do repositório para armazenar produtos"""

    @abstractmethod
    def save(self, produto: Product):
        pass

    @abstractmethod
    def search_by_text(self, termo: str):
        pass

    @abstractmethod
    def autocomplete(self, termo: str):
        pass
