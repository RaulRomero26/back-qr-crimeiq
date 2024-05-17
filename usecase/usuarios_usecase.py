from repositories.usuarios_repository import usuarios_repository
from werkzeug.utils import secure_filename
import os

class UsuariosUsecase:

    def __init__(self, usuarios_repository):
        self.usuarios_repository = usuarios_repository

    def registrar_usuario(self, usuario_data, archivos_data):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        
        print("Directorio actual:", directorio_actual)
        upload_folder = os.path.join(os.path.dirname(os.path.dirname(directorio_actual)), 'USUARIOS')
        print("Upload folder:", upload_folder)
        print(archivos_data)  # Verificar que los archivos se están recibiendo

        for file_key in archivos_data:
            file = archivos_data[file_key]
            if file and file.filename:
                filename = secure_filename(file.filename)
                save_path = os.path.join(directorio_actual, '..', 'USUARIOS', filename)
                file.save(save_path)
                usuario_data['Foto'] = f"http://localhost:5000/imagenes/usuarios/{filename}"

        return self.usuarios_repository.registrar_usuario(usuario_data)
        
    def get_usuarios(self):
        return self.usuarios_repository.getUsuarios()

usuarios_usecase = UsuariosUsecase(usuarios_repository)