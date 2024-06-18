import os
from usecase.tareas_usecase import tareas_usecase
def job():
    # Solo ejecutar en el proceso principal
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        lista = tareas_usecase.get_task_recurrente()
        print(lista)

        #print('Job executed')
