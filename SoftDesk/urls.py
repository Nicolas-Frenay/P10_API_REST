"""SoftDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.projects.views import ProjectViewset
from apps.authentication.views import RegisterView
from apps.contributors.views import UserViewset
from apps.issues.views import IssueViewset
from apps.comments.views import CommentViewset
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewset, basename='project_list')

users_router = routers.NestedSimpleRouter(router, r'projects',
                                          lookup='project')
users_router.register(r'users', UserViewset, basename='users')

issues_router = routers.NestedSimpleRouter(router, r'projects',
                                           lookup='project')
issues_router.register(r'issues', IssueViewset, basename='issues')

comments_router = routers.NestedSimpleRouter(issues_router, r'issues',
                                             lookup='issue')
comments_router.register(r'comments', CommentViewset, basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/', include(users_router.urls)),
    path('api/', include(issues_router.urls)),
    path('api/', include(comments_router.urls)),
    path('api/login/', TokenObtainPairView.as_view(),
         name='token_obtains_pairs'),
    path('api/login/refresh/', TokenRefreshView.as_view(),
         name='refresh_token'),
    path('api/signup/', RegisterView.as_view(), name='auth_register')
]
