from repositories.auth_repository import auth_repository

class AuthUsecase:

    def __init__(self, auth_repository):
        self.auth_repository = auth_repository

    def login(self, login_data):
        return self.auth_repository.login(login_data)
        

auth_usecase = AuthUsecase(auth_repository)