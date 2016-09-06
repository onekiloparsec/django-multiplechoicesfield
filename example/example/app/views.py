# -*- coding: utf-8 -*-


from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def app_index(request):
    user = User.objects.get(username='admin')
    if not hasattr(user, 'backend'):
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
    login(request, user)
    return HttpResponseRedirect(reverse('admin:app_book_change', args=(1,)))
