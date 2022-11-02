from django.urls import path,include
from . import views
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.contrib.staticfiles.urls import static
from django.views.decorators.cache import cache_page
import debug_toolbar
router=DefaultRouter()
router.register('api/vehciles',views.vehcilesinfo)
router.register('api/cars',views.carsinfo)
router.register('api/trucks',views.trucksinfo)
router.register('api/students',views.studentsinfo)
router.register('api/payment',views.paymentinfo)
#router.register('api/trsdemo',views.trsdemo,basename='trsdemo')
#router.register('myobjects',views.objcount)
urlpatterns = [
path('info/',views.home_view),
path('trucks/',views.truck_view),
path('cars/',views.car_view),
path('vehciles/',views.vehicle_view),
path('',include(router.urls)),
path('auth/',include('rest_framework.urls')),
path('students/',views.student_view),
path('payment/',views.payment_view),

path('api/trsdemo',cache_page(60*2)(views.trsdemo.as_view()),name='trsdemo'),
path("sync/", views.sync_view),
path('file/',views.file_handler),
#------------------ORM--------------------------------------------------------------------------------
path('Scenario1/<int:pk>/',views.Scenario1.as_view()),
path('Scenario2/',views.Scenario2),
path('Scenario5/',views.Scenario5.as_view()),
path('print/',views.update),
path('Scenario6/',views.Scenario6.as_view()),
path('Scenario9/',views.Scenario9.as_view()),
path('myobjects/<int:pk>/',views.Scenario11.as_view()),

path('__debug__/',include(debug_toolbar.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)