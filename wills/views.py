from django.shortcuts import render, redirect, get_object_or_404
from .models import ClientRequest
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
import os


def home(request):
    requested = False
    if request.method == "POST":
        if 'questionnaire' in request.POST:
            name = request.POST['name']
            email = request.POST['email'].lower()

            if email not in list(ClientRequest.objects.all().values_list('email', flat=True)):
                newclientrequest = ClientRequest.objects.create(name=name, email=email)

            file_path = os.path.join(settings.BASE_DIR, 'ESTATE PACKAGE QUESTIONNAIRE.docx')

            email = EmailMessage(
                f"Dear {name}, here is the questionnaire you requested.",
                    """<h1>Thank you for your interest.</h1>

                    <p>Attached is your requested Estate Package Questionnaire.</p>

                    <p>Fill out the questionnaire as best as you can, and we can discuss your instructions once you've filled it out.</p>

                    <p>Once the questionnaire is filled out, please send it to calgarymobilewills@gmail.com</p>

                    <p>If you have any questions, please contact us by phone at <strong>403-629-8556</strong> or reply to this email, and we will get back to you as soon as possible.</p>
                    """,
                'settings.EMAIL_HOST_USER',
                [email],
            )
            email.content_subtype = 'html'

            with open(file_path, 'rb') as f:
                email.attach(os.path.basename(file_path), f.read(), 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')

            email.send()
            # send_mail(
            #     f"Dear {name}, here is the questionaire you requested.",
            #     f"Fill out the form as best as you can, and we can discuss your instructions once you've filled them out.\n\nIf you have any questions, please contact 403-629-8556 or reply to this email, and we will get back to you as soon as possible.",
            #     'settings.EMAIL_HOST_USER',
            #     [email],
            #     fail_silently=False
            # )
            if name and email:
                requested = True
                # return render(request, 'home.html', {'requested':requested})
                return redirect('thankyou')

        if 'contact' in request.POST:
            contact_name = request.POST['contact_name']
            contact_email = request.POST['contact_email'].lower()
            contact_message = request.POST['contact_message']

            email_for_contact = EmailMessage(
                f"A message from {contact_name}",
                f"""
                This message is sent from contact form from www.calgarymobilewills.ca

                <h3>Client name : </h3>

                {contact_name}

                <h3>Client message : </h3>

                {contact_message}

                <h3>Client email :</h3>

                {contact_email}
                """,
                'settings.EMAIL_HOST_USER',
                ['calgarymobilewills@gmail.com'],
            )
            email_for_contact.content_subtype = 'html'
            email_for_contact.send()

            print(contact_name, contact_email, contact_message)
            if contact_name and contact_email and contact_message:
                return redirect('thankyou_contact')
    requested = False
    context = {'requested': requested}
    return render(request, 'home.html', context)

def thankyou(request):
    return render(request, 'thankyou.html',)

def thankyou_contact(request):
    return render(request, 'thankyou2.html',)

def page_not_found_view(request, exception):
       return render(request, 'page_not_found.html')