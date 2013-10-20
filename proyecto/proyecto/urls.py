from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#PERMITE USAR LA CLASE DE VIEWS TEMPLATES PARA SER REUTILIZADAS
from django.views.generic import TemplateView

#OBTENEMOS EL LISTVIEWS DEL VIEW.PY QUE CREAMOS
from app.views import EnlaceListView, EnlaceDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name="home"),

    url(r'^plus/(\d+)$', 'app.views.plus', name="plus"),
    url(r'^minus/(\d+)$', 'app.views.minus', name="minus"),

    url(r'^categoria/(\d+)$', 'app.views.categoria', name="categoria"),

    #urls para el formulario
    url(r'^add/$','app.views.add', name="add"),

    #REUSAMOS LA PLANTILLA INDEX.HTML
    url(r'^about/$',TemplateView.as_view(template_name='index.html'),name='about'),

    #GENERAMOS LA URL DEL LISTVIEWS enlace
    url(r'^enlaces/$',EnlaceListView.as_view(),name='enlaces'),

    #MEDIANTE UNA EXPRESION REGULAR OBTENEMOS EL id DEL ENLACE
    url(r'^enlaces/(?P<pk>[\d]+)$',EnlaceDetailView.as_view(),name='enlace'),

    # url(r'^proyecto/', include('proyecto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
