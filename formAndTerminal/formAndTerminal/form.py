from django import forms

class MakerspaceForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    id = forms.IntegerField()
    
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        id = self.cleaned_data['id']

        # send email
        print(name, email, phone, id)

        return True