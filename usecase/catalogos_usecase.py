from repositories.catalogos_repository import catalogos_repository

class CatalogosUsecase:

    def __init__(self, catalogos_repository):
        self.catalogos_repository = catalogos_repository

    def catalogo_usuarios(self):
        return catalogos_repository.catalogo_usuarios()
    
    def get_catalogo(self, catalogo_buscado):
        return catalogos_repository.get_catalogo(catalogo_buscado)
    
    def update_catalogo(self, catalogo_data):
        return catalogos_repository.update_catalogo(catalogo_data)

catalogos_usecase = CatalogosUsecase(catalogos_repository)