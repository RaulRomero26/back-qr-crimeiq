from repositories.reportes_repository import reportes_repository

class ReportesUsecase:

    def __init__(self, reportes_repository):
        self.reportes_repository = reportes_repository

    def guardar_reporte(self, reporte_data):  # Añade 'self' aquí
        return reportes_repository.guardar_reporte(reporte_data)
    
    def guardar_alerta(self, alerta_data):
        return reportes_repository.guardar_alerta(alerta_data)
    
    def get_alertas(self):
        return reportes_repository.get_alertas()

    def get_incidentes(self):
        return reportes_repository.get_incidentes()

reportes_usecase = ReportesUsecase(reportes_repository)