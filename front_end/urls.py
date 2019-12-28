from django.conf.urls import url
from front_end import views

urlpatterns=[
    url(r'^$',views.webPage),
    url(r'^messages/$',views.messagePage)
]