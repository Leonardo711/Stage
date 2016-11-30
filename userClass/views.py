#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User,Group
from .forms import *
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

##### Email validation ###
from itsdangerous import URLSafeSerializer as utsr
from itsdangerous import TimestampSigner
import base64

from django.conf import settings as django_settings
from django.utils.translation import ugettext as _

class Token:
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodestring(security_key)
    def generate_validate_token(self, username):
        serializer = utsr(self.security_key)
        timeStamp = TimestampSigner(self.security_key)
        username = timeStamp.sign(username)
        return serializer.dumps(username, self.salt)
    def confirm_validate_token(self, token, expiration=3600):
        serializer = utsr(self.security_key)
        timeStamp = TimestampSigner(self.security_key)
        username = serializer.loads(token, salt = self.salt)
        username = timeStamp.unsign(username, max_age=expiration)
        print(username)
        return username


    def remove_validate_token(self, token):
        serializer = utsr(self.security_key)
        timeStamp = TimestampSigner(self.security_key)
        username = serializer.loads(token, salt = self.salt)
        username = timeStamp.unsign(username)
        return username

# a global variable
token_confirm = Token(django_settings.SECRET_KEY)
# Create your views here.
class signup(TemplateView):
    form_class = SignUpForm
    template_name = "userClass/signup.html"

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        print request.GET
        return self.render_to_response(self.get_context_data(form = form))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.render_to_response(self.get_context_data(form = form))
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = username
            try:
                user = User.objects.create_user(username = username, password=password, email=email)
            except:
                message=_(u"account exists")
                return self.render_to_response(self.get_context_data(form=form, user_message=message))
            user.is_active = False
            user.save()
            token = token_confirm.generate_validate_token(username)
            message = "\n".join([_(u'welcome to register our stage '), _(u'please check your email to accomplish the registeration'),
                                 "http://"+'/'.join([django_settings.DOMAIN, 'accounts','activate', token])])
            send_mail(_(u'registration information'), message,django_settings.EMAIL_HOST_USER, [email])
            user.groups.add(Group.objects.get(name="registedUser"))
            return render(request, "userClass/signUpSuccess.html")

def active_user(request, token):
    #print(token)
    try:
        username = token_confirm.confirm_validate_token(token)
    except:
        username = token_confirm.remove_validate_token(token)
        users = User.objects.filter(username=username)
        for user in users:
            user.delete()
        return HttpResponse(_("sorry, the link is out-of-date"))
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(_("sorry, the user does not exist"))
    user.is_active = True
    user.save()
    return HttpResponse(_("Validation success"))

