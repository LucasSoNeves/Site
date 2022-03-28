from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    send = False
    
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #enviar e-mail
        nome = request.POST.get('nome','')
        email = request.POST.get('email','')
        mensagem = request.POST.get('mensagem','')
        email = EmailMessage(
            "Mensagem do Blog Django",
            "De {} <{}> Escreveu: \n\n{}".format(nome,email,mensagem),
            "nao-responder@inbox.mailtrap.io",
            ["lucas.neves.ead@gmail.com"],
            reply_to=[email]     
        )
        try:
            email.send()
            send = True
        except:
            send = False       
    
    context = {
        'form':form,
        'success':send
    }
    return render(request,'contact/contact.html',context)    
