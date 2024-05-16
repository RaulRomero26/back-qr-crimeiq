from repositories.catalogos_repository import catalogos_repository

class CatalogosUsecase:

    def __init__(self, catalogos_repository):
        self.catalogos_repository = catalogos_repository

    def catalogo_usuarios(self):
        return catalogos_repository.catalogo_usuarios()

catalogos_usecase = CatalogosUsecase(catalogos_repository)