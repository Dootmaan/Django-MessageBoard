from django.conf.urls import url
from back_end import views

urlpatterns=[
    url(r'response/$',views.response),
    url(r'loadMessages',views.loadMessages)
]