from django.urls import path,include,re_path
from rest_framework import permissions

from . import views
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.contrib.staticfiles.urls import static
from django.views.decorators.cache import cache_page
import debug_toolbar
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

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
path('accounts/',include('rest_framework.urls')),
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
path('Scenario10/',views.Scenario10.as_view()),
path('myobjects/<int:pk>/',views.Scenario11.as_view()),

re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
path('__debug__/',include(debug_toolbar.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
