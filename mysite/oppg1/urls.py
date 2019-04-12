# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:49:06 2019

@author: eila2903
"""

from django.conf.urls import url, include
from oppg1 import views # Viktig å huske å importere views for å kunne linke til funksjonene i views.py


urlpatterns = [
      url('', views.index, name="index")
      # Her sendes requesten videre til funksjonen index i fila views.py
]