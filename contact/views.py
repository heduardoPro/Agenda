from django.shortcuts import render, redirect

# Create your views here.

from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form,
        }

    if form.is_valid():
        form.save()
        return redirect('contact:create')
    
    return render(
        request,   
        'contact/create.html',
    )
