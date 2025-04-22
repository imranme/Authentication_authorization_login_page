from django.shortcuts import render
import .forms import RegistrForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            print(form.cleaned_data)
        else:
            form = RegistrForm()
        return render(request, './home.html'{'form': form})
        
