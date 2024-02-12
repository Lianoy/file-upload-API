from filetest.celery import app
from .models import File
from time import sleep

@app.task()
def processing_file(file_id):
    # working_file = File.objects.get(id=file_id) ##Эта строчка нужна, если есть действия с файлом, а не просто сон
    sleep(60) ### Происходит условная обработка файла
    File.objects.filter(id=file_id).update(processed = True)
    return file_id