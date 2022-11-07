from django.conf import settings
from django.contrib.auth import logout
from django.db import connections
from django.db.models import Q
from django.http import (
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.middleware.locale import LocaleMiddleware
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


'''class EncryptMiddleware(MiddlewareMixin):
    def get_response(self,request,response):'''


