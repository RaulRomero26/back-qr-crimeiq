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
    
    def add_option(self, catalogo_data):
        return catalogos_repository.add_option(catalogo_data)

    def get_catalogo_activo(self, catalogo_buscado):
        return catalogos_repository.get_catalogo_activos(catalogo_buscado)

catalogos_usecase = CatalogosUsecase(catalogos_repository)