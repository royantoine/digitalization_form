from django.shortcuts import render, redirect
from models import Document

def document_list(request):
    documents = Document.objects.all()
    return render(
        request, 
        'document/document_list.html',
        {'documents': documents}
    )

def document_detail(request, id):
    document = Document.objects.get(id=id)
    return render(request,
          'document/document_detail.html',
         {'document': document})

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save()
            return redirect('document-detail', document.id)

    else:
        form = DocumentForm()

    return render(request,
            'document/document_create.html',
            {'form': form})

def document_update(request, id):
    document = Document.objects.get(id=id)

    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document-detail', document.id)
    else:
        form = DocumentForm(instance=document)

    return render(request,
                'listings/document_update.html',
                {'form': form})

def document_delete(request, id):
    document = Document.objects.get(id=id)  

    if request.method == 'POST':
        document.delete()
        return redirect('document-list')

    return render(request,
                    'listings/document_delete.html',
                    {'document': document})
