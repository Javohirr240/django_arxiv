from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.views.generic import ListView
from .models import Contact

class IndexView(TemplateView):
  template_name = 'index.html'

class ContactPageView(TemplateView):
  success_message = None
  def get(self, request, *args, **kwargs):
    form = ContactForm()
    context = {
      'form': form,
    }
    return render(request, 'index.html', context)

  def post(self, request, *args, **kwargs):
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      form = ContactForm()
      success_message = "Biz bilan bog'langaningiz uchun tashakkur!"
      # success_url = 'list'
      return redirect('list')
    else:
      success_message = "Forma to'liq to'ldirilmagan!"
    context = {
      'form': form,
      'success_message':success_message,
    }
    return render(request, 'index.html', context= context)
#
# class Xabarlar(ListView):
#   model = Contact
#   template_name = 'list.html'

class Xabarlar(TemplateView):
  def get(self, request, *args, **kwargs):
    new = Contact.objects.all()
    context = {
      'new':new,
    }
    return render(request, 'list.html', context)
