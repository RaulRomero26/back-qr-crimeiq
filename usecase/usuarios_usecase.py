from repositories.usuarios_repository import usuarios_repository

class UsuariosUsecase:

    def __init__(self, usuarios_repository):
        self.usuarios_repository = usuarios_repository

    def registrar_usuario(self, usuario_data):
        return self.usuarios_repository.registrar_usuario(usuario_data)
        
    def get_usuarios(self):
        return self.usuarios_repository.getUsuarios()

usuarios_usecase = UsuariosUsecase(usuarios_repository)