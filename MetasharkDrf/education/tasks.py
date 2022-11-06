import time
from MetasharkDrf.celery import app
from education.services import report_to_exel


@app.task
def report_task():
    """
    Функция запускает создание отчёта в фоновом режиме
    :return:
    """
    report_to_exel()
