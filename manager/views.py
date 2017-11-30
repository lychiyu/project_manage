# -*- coding: utf-8 -*-

from random import Random

from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.http import JsonResponse
from models import *


def send_email(email, email_title, email_body):
    # subject, from_email, to = email_title, settings.EMAIL_FROM, email
    msg = EmailMultiAlternatives(email_title, email_body, settings.EMAIL_FROM, [email])
    msg.attach_alternative(email_body, "text/html")
    msg.send()
    # send_mail(email_title, email_body, 'jgsuitclub@qq.com', [email])


def report_exp(request):
    project_name = request.POST['project_name']
    content = request.POST['content']
    group_id = request.POST.get('group_id')

    project = ProjectInfo.objects.filter(name=project_name, status=1).first()
    if not project:
        return JsonResponse({'code': 0})

    emails = []
    if group_id:
        group = GroupInfo.objects.filter(id=group_id, project=project, status=1).first()
        users = group.members.all()
        for user in users:
            emails.append(user.email)
    else:
        groups = GroupInfo.objects.filter(project=project, status=1)
        for group in groups:
            users = group.members.filter(status=1)
            for user in users:
                emails.append(user.email)

    email_title = project.display_name + u'消息----报错了，急需解决！！！！'
    for email in emails:
        send_email(email, email_title, content)

    return JsonResponse({'code': 0})
