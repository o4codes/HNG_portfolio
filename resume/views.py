from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail#import messages

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        to = request.POST['email']
        try:
            form.save()
            form = ContactForm()
            messages.success(request,"Form saved")
            send_mail('o4codes software dev', 'Message is recieved. You will be contacted in due time', 'oforkansi.shadrach@gmail.com', [to,], fail_silently=False)
            print("mail should have been sent")
            print(to)
        except Exception as e:
            print("something is wrong")
            print(e)
        finally:
            return redirect("home")
    context = {'form':form}
    
    return render(request, "contact.html", context)