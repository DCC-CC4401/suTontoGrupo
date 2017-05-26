# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )
    tipo = models.CharField(max_length=50)


class Vendedor(models.Model):
    user = models.OneToOneField(UserInfo,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )


class VendedorAmbulante(Vendedor):
    check_in = models.BooleanField


class VendedorFijo(Vendedor):
    apertura = models.TimeField
    cierre = models.TimeField


class Favoritos(models.Model):
    alumno = models.OneToOneField(UserInfo,
                                  on_delete=models.CASCADE,
                                  primary_key=False,
                                  )
    favorito = models.OneToOneField(Vendedor,
                                    on_delete=models.CASCADE,
                                    primary_key=False
                                    )



