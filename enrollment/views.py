from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import RegisterForm

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            father_name = form.cleaned_data['father_name']
            birth_year = form.cleaned_data['birth_year']
            primary_number = form.cleaned_data['primary_phone']
            is_whatsapp = form.cleaned_data['is_whatsapp']
            whatsapp_number = form.cleaned_data['whatsapp_number']
            hs_year = form.cleaned_data['hs_year']
            enroll_year = form.cleaned_data['enroll_year']
            stream = form.cleaned_data['stream']
            current_profession = form.cleaned_data['current_profession']

            ### Need this data to save in the the database
            print(name, email, gender, father_name, birth_year, primary_number, is_whatsapp, whatsapp_number, hs_year, enroll_year, current_profession)


            messages.success(request, "Thank you! You're successfully registered")
            
            return redirect('/enrollment')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})