from rest_framework import routers
from apis.views import SchoolUserViewSet,StudentUserViewSet

router = routers.DefaultRouter()
router.register(r'school', SchoolUserViewSet)
router.register(r'student',StudentUserViewSet)

urlpatterns = [
    path(r'',include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),
    url('^liststudents/(?P<schoolid>\d+)/$',liststudents.as_view()),
]