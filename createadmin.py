#!/usr/bin/env python
from django.contrib.auth.models import User
u, created = User.objects.get_or_create(username='admin')
if created:
    u.set_password('password')
    u.is_superuser = True
    u.is_staff = True
    u.save()
# Remember to change this password after the deploy!
