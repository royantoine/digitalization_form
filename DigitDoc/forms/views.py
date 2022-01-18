from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
 
# Create your views here.
from forms.forms import InputForm
 
# view for the index page
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'document_list'
    template_name = 'home.html'
 
    def get_queryset(self):
        return InputForm.objects.all()
 
# view for the product entry page
class DocumentEntry(CreateView):
    model = InputForm
    # the fields mentioned below become the entry rows in the generated form
    fields = ['document_name', 'value']
 
# view for the product update page
class DocumentUpdate(UpdateView):
    model = InputForm
    # the fields mentioned below become the entyr rows in the update form
    fields = ['document_name', 'value']
 
# view for deleting a product entry
class DocumentDelete(DeleteView):
    model = InputForm
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('forms:home')