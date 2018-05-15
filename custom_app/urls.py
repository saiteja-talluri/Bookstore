# -*- coding: utf-8 -*-
## @brief urls for the Custom app.
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='user_list'
    ),
]
