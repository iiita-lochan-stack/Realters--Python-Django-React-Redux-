import email
from logging import exception
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, requests, format=None):
        data = self.request.data

        import pdb;
        # pdb.set_trace()

        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                + '\nEmail: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                'iiita.guptalochan@gmail.com',
                ['iiita.guptalochan@gmail.com'],
                fail_silently=False
            )
            
            contact = Contact(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
            contact.save()

            return Response({'success': 'Message sent successfully'})

        except Exception as e:
            return Response({'error': 'Message Failed to send because of ' + str(e)})
