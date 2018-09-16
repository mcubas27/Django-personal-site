from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.
def index(request):
    context = {"home_page": "active"}
    return render(request, 'pages/index.html', context)
def about(request):
    context = {"about_page": "active"}
    return render(request, 'pages/about.html', context)
def contact(request):
    context = {"contact_page": "active"}
    return render(request, 'pages/contact.html', context)


def emailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subjet = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subjet, message, from_email, ['mach_278@hotmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, "pages/index.html", {'form': form})



def successView(request):
    return render(request, 'pages/success.html')
