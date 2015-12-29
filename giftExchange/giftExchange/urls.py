"""giftExchange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

exchangepatterns = [
    url(r'create/', 'santa_gift_exchange.views.exchange'),
    url(r'join/', 'santa_gift_exchange.views.joinexchange'),
    url(r'^(?P<exchange_id>\d+)/addsanta/', 'santa_gift_exchange.views.addsanta'),
    url(r'^(?P<exchange_id>\d+)/$', 'santa_gift_exchange.views.exchangeprofile', name='exchange'),
]

userpatterns = [
    url(r'^(?P<user_nameid>\d+)/$', 'santa_gift_exchange.views.profile', name='profile'),
    url(r'^(?P<user_nameid>\d+)/updateprofile/$', 'santa_gift_exchange.views.updateprofile', name='edit_profile'),
    url(r'^(?P<user_nameid>\d+)/updatedislike/$',
        'santa_gift_exchange.views.updatedislike',
        name='edit_dislike_profile'),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'santa_gift_exchange.views.register_user', name='signup'),
    url(r'^sign_up/', 'santa_gift_exchange.views.register_user'),
    url(r'^login/', 'santa_gift_exchange.views.login_user'),
    url(r'^logout/$', 'santa_gift_exchange.views.user_logout', name='logout'),
    url(r'^home/', 'santa_gift_exchange.views.home'),
    # url(r'^exchange/(?P<name>\w+)/', include(exchangepatterns, namespace="excange_urls")),
    url(r'^exchange/', include(exchangepatterns, namespace='exchange_urls')),
    url(r'profile/', include(userpatterns, namespace='profile_urls'))
    # url(r'^confirm/(?P<activation_key>\w+)/', 'santa_gift_exchange.views.register_confirm'),
]

# 'santa_gift_exchange.views.exchange'