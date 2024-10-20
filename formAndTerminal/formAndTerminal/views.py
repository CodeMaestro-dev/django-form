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
            # Save form data to session
            request.session['name'] = form.cleaned_data['name']
            request.session['email'] = form.cleaned_data['email']
            request.session['phone'] = form.cleaned_data['phone']
            request.session['id'] = form.cleaned_data['id']
            
            # Send email
            form.send_email()

            return redirect('contact-success')
    else:
        form = MakerspaceForm()

    context = {'form': form}
    return render(request, 'contact.html', context)


# This is to define the contact_success function to handle success page form
def success_view(request):
    # Retrieve session data
    name = request.session.get('name')
    email = request.session.get('email')
    phone = request.session.get('phone')
    student_id = request.session.get('id')

    # Pass these values to the template context
    context = {
        'name': name,
        'email': email,
        'phone': phone,
        'id': student_id,
    }

    return render(request, 'success.html', context)