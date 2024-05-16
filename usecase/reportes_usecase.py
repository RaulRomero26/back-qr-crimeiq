
from repositories.reportes_repository import reportes_repository

class ReportesUsecase:

    def __init__(self, qr_repository):
        self.qr_repository = qr_repository

    def guardar_reporte(self,reporte_data):
        return reportes_repository.guardar_reporte(reporte_data)
    
    def guardar_alerta(self,alerta_data):
        return reportes_repository.guardar_alerta(alerta_data)

reportes_usecase = ReportesUsecase(reportes_repository)