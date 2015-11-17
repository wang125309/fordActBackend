from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^backend/loginAction/', 'backend.views.loginAction'),
    url(r'^backend/quitAction/', 'backend.views.quitAction'),
    url(r'^backend/getNewsList/', 'backend.views.getNewsList'),
    url(r'^backend/addNews/', 'backend.views.addNews'),
    url(r'^backend/editNews/', 'backend.views.editNews'),
    url(r'^backend/deleteNews/', 'backend.views.deleteNews'),
    url(r'^backend/getNewsById/', 'backend.views.getNewsById'),
    url(r'^backend/getProductList/', 'backend.views.getProductList'),
    url(r'^backend/addProduct/', 'backend.views.addProduct'),
    url(r'^backend/editProduct/', 'backend.views.editProduct'),
    url(r'^backend/deleteProduct/', 'backend.views.deleteProduct'),
    url(r'^backend/getProductById/', 'backend.views.getProductById'),
    url(r'^backend/getCulList/', 'backend.views.getCulList'),
    url(r'^backend/editCul/', 'backend.views.editCul'),
    url(r'^backend/getCulById/', 'backend.views.getCulById'),

)
