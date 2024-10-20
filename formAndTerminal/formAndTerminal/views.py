from django.shortcuts import render, redirect
from .form import MakerspaceForm

# This is the home page view function
def home_view(request):
    return render(request, 'index.html')

# This is to define the contact _view function to handle contact form
def contact_view(request):  
    form = MakerspaceForm()
    if request.method == 'POST':
        form = MakerspaceForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = MakerspaceForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

# This is to define the contact_success function to handle success page form
def success_view(request):
    return render(request, 'success.html')
