import os
from documents.models import Document


def create_document_from_folder(form):
    folders = os.listdir(form['path'].value())
    for folder in folders:
        document = Document(path=os.path.join(form['path'].value(), folder)) 
        document.save()
    return True 