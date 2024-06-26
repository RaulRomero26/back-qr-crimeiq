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

        usuario_data['Foto'] = "https://api.scanner.crimeiq.org/imagenes/usuarios/default.svg"
        usuario_data['Nom_completo'] = usuario_data['Nombre'] + ' ' + usuario_data['Ap_paterno'] + ' ' + usuario_data['Ap_materno']
        usuario_data['activo'] = True
        print('QUE HAY EN USUSARIOS DATA')
        print(usuario_data)
        
        for file_key in archivos_data:
            file = archivos_data[file_key]
            if file and file.filename:
                filename = secure_filename(file.filename)
                save_path = os.path.join(directorio_actual, '..', 'USUARIOS', filename)
                file.save(save_path)
                usuario_data['Nom_completo'] = usuario_data['Nombre'] + ' ' + usuario_data['Ap_paterno'] + ' ' + usuario_data['Ap_materno']
                usuario_data['Foto'] = f"https://api.scanner.crimeiq.org/imagenes/usuarios/{filename}"

        return self.usuarios_repository.registrar_usuario(usuario_data)
        
    def get_usuarios(self):
        return self.usuarios_repository.getUsuarios()

    def get_usuarios_asignados(self, serv_asignado):
        return self.usuarios_repository.get_usuarios_asignados(serv_asignado)

    def actualizar_usuario(self, usuario_data, archivos_data):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        
        print("Directorio actual:", directorio_actual)
        upload_folder = os.path.join(os.path.dirname(os.path.dirname(directorio_actual)), 'USUARIOS')
        print("Upload folder:", upload_folder)
        
        print('QUE HAY EN USUSARIOS DATA')
        print(usuario_data)
        if archivos_data:
             for file_key in archivos_data:
                file = archivos_data[file_key]
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    save_path = os.path.join(directorio_actual, '..', 'USUARIOS', filename)
                    file.save(save_path)
                    usuario_data['Nom_completo'] = usuario_data['Nombre'] + ' ' + usuario_data['Ap_paterno'] + ' ' + usuario_data['Ap_materno']
                    usuario_data['Foto'] = f"https://api.scanner.crimeiq.org/imagenes/usuarios/{filename}"
                    usuario_data['activo'] = True

        return self.usuarios_repository.actualizar_usuario(usuario_data)

usuarios_usecase = UsuariosUsecase(usuarios_repository)