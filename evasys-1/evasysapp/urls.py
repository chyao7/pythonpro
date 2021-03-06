from evasysapp import views
from django.conf.urls import url,include

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^home/', views.home),
    url(r'^defindex/', views.defindex),
    url(r'^chanindex/', views.chanindex),
    url(r'^creaindex/',views.creaindex),
    url(r'^detail/',views.detail),
    url(r'^sendecode/',views.sendecode),
    url(r'^register/',views.register),
    url(r'^sucregister/',views.sucregister),
    url(r'^modscope/',views.modscope),
    url(r'^modalgorithm/',views.modalgorithm),
    url(r'^moddescribe/',views.moddescribe),
    url(r'^modevaluation/',views.modevaluation),
    url(r'^indexval/',views.indexval),
    url(r'^newindex/',views.newindex),
    url(r'^calculate/',views.calculate),
    url(r'^resvisualization/',views.resvisualization),
    url(r'^resshow/',views.resshow),
    url(r'^EXEMtheory/',views.EXEMtheory),
    url(r'^EXEMfeature/',views.EXEMfeature),
    url(r'^EXEMmodel/',views.EXEMmodel),
    url(r'^EWMtheory/',views.EWMtheory),
    url(r'^EWMfeature/',views.EWMfeature),
    url(r'^EWMmodel/',views.EWMmodel),
    url(r'^AHPtheory/',views.AHPtheory),
    url(r'^AHPfeature/',views.AHPfeature),
    url(r'^AHPmodel/',views.AHPmodel),
    url(r'^CMtheory/',views.CMtheory),
    url(r'^CMfeature/',views.CMfeature),
    url(r'^CMmodel/',views.CMmodel),
    url(r'^getexcel/',views.getexcel),
    url(r'^Usercenter/', views.Usercenter),
    url(r'^sendecode_email_change/', views.sendecode_email_change),
    url(r'^company_info/', views.company_info),
    url(r'^company_del/', views.company_del),
    url(r'^email_info/', views.email_info),
    url(r'^code_info/', views.code_info),
    url(r'^user_feedback/', views.user_feedback),
    url(r'^historical_eval/', views.historical_eval),
]