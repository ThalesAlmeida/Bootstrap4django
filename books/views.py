from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Author
from django.utils import timezone
from django.shortcuts import get_object_or_404

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'
    template_name_suffix = '_update_form'

class AuthorListView(ListView):
    model = Author
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
    template_name_suffix = '_confirm_delete'

