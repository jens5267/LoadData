from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from .models import Load
from .forms import LoadForm

# Create your views here.
def load_detail_view(request):
    try:
        obj = Load.objects.get(id=1)
        context = {
            'object': obj
        }
    except ObjectDoesNotExist:
        context = {}
    return render(request, 'loads/load_detail.html', context)

def load_create_view(request):
    form = LoadForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'loads/load_create.html', context)