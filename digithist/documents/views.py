from telnetlib import DO
from django.http import HttpResponse
from django.shortcuts import render, redirect
from documents.models import Document, Folder
from documents.forms import DocumentForm, FolderForm
from django.contrib import messages 
from django.core.exceptions import ObjectDoesNotExist
from documents.utils import create_document_from_folder
import os
import csv
from documents.models import Document

def document_list(request):
    documents = Document.objects.all()
    return render(
        request, 
        'documents/document_list.html',
        {'documents': documents}
    )

def document_detail(request, id):
    try:
        document = Document.objects.get(id=id)
        path_files = [os.path.join(document.path, path_file) for path_file in os.listdir(document.path)]
        path_files.sort()
        next_document = document.id + 1
        previous_document = document.id - 1
        return render(request,
            'documents/document_detail.html',
            {
                'document': document, 
                'path_files': path_files, 
                'next_document': next_document, 
                'previous_document': previous_document
                })
    except ObjectDoesNotExist:
        return HttpResponse("Document does not Exist") 

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save()
            return redirect('document-detail', document.id)

    else:
        form = DocumentForm()

    return render(request,
            'documents/document_create.html',
            {'form': form})

def document_update(request, id):
    document = Document.objects.get(id=id)
    path_files = [os.path.join(document.path, path_file) for path_file in os.listdir(document.path)]
    path_files.sort()
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document-detail', document.id)
    else:
        form = DocumentForm(instance=document)

    return render(request,
                'documents/document_update.html',
                {'form': form, 'path_files': path_files, "document": document})

def document_delete(request, id):
    document = Document.objects.get(id=id)  

    if request.method == 'POST':
        document.delete()
        return redirect('document-list')

    return render(request,
                    'documents/document_delete.html',
                    {'document': document})

def folder_create(request):
    if request.method == 'POST':
        all_folder = Folder.objects.all()
        existing_folders = [folder.path for folder in all_folder]
        form = FolderForm(request.POST)
        if form.is_valid():
            if form['path'].value() not in existing_folders:
                form.save()
                create_document_from_folder(form)
                return redirect('document-list')
            else:
                messages.error(request, "Ce dossier a déjà été ajouté")
    else:
        form = FolderForm()

    return render(request,
            'documents/document_create.html',
            {'form': form})

def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Type', 'Description', 'Value', 'Path', 'Name'])
    for doc in Document.objects.all().values_list(
        'type', 'description', 'value', 'path', 'name'
        ):
        writer.writerow(doc)
    response['Content-Disposition'] = 'attachment; filename="documents.csv'
    return response