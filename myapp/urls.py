from django.conf.urls import url
from.import views


urlpatterns=[
    url(r'^home/',views.home),
    url(r'^courses/',views.courses),
    url(r'^safetyrules/',views.safetyrules),
    url(r'^contact/', views.contact),
    url(r'^findus/', views.findus),
    url(r'^about/', views.about),
    url(r'^Schedule/', views.Schedule),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^machine1/', views.m1),
    url(r'^machine2/', views.m2),
    url(r'^machine3/', views.m3),
    url(r'^machine4/', views.m4),
    url(r'^machine5/', views.m5),
    url(r'^gallery/', views.gallery),
]