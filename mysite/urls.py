
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blog.urls')),
    url(r'^chat/',include('django_private_chat.urls')),
    url(r'^chat/', include('custom_app.urls'))
    
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
