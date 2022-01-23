from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

# Create your views here.
def Index(request):
    '''
    response = HttpResponse()
    response.writelines('<h1>Welcome to Django</h1>')
    response.write('This is a App Home')
    return response
    '''
    return render(request, 'Pages/Home.html')

# def Blog(request):
#     return render(request, 'Pages/Blog.html')


def Contact(request):
    return render(request, 'Pages/Contact.html')


def Error(request, *args, **kwargs):
    return render(request, 'Pages/Error.html')


def register(request):

    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'Pages/Register.html', {'form': form})