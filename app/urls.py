
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views_serializers
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard'),
    path('brands/', views.brands, name='brands'),
    path('brands_detail/<int:brand_id>/', views.brands_detail, name='brands_detail'),
    path('login/', views.user_login, name='login'),
    path('category/<int:cat_id>/', views.category, name='category'),
    path('subcategory/<int:subcat_id>/', views.subcategory, name='subcategory'),
    path('news/', views.news, name='news'),
    path('news/<int:news_id>/', views.news, name='news'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('by_categories/<int:cat_id>/', views.by_categories, name='by_categories'),

    path('inforeklam/<int:pk>/', views.infoView.as_view(), name='infoReklams'),
    path('inforeklam/', views.infoView.as_view(), name='infoReklams'),

    path('infofirm/<int:pk>/', views.infoFirmReklams.as_view(), name='infoFirmReklams'),

    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),

    url(r'^brand-list/$', views_serializers.BrandList.as_view(), name=views_serializers.BrandList.name),
    url(r'^brand-list/(?P<pk>[0-9]+)$', views_serializers.BrandDetail.as_view(), name=views_serializers.BrandDetail.name),
    url(r'^reklam-list/$', views_serializers.ReklamList.as_view(), name=views_serializers.ReklamList.name),
    url(r'^reklam-list/(?P<pk>[0-9]+)$', views_serializers.ReklamDetail.as_view(), name=views_serializers.ReklamDetail.name),
    url(r'^color-list/$', views_serializers.ColorList.as_view(), name=views_serializers.ColorList.name),
    url(r'^color-list/(?P<pk>[0-9]+)$', views_serializers.ColorDetail.as_view(), name=views_serializers.ColorDetail.name),
    url(r'^gender-list/$', views_serializers.GenderList.as_view(), name=views_serializers.GenderList.name),
    url(r'^gender-list/(?P<pk>[0-9]+)$', views_serializers.GenderDetail.as_view(), name=views_serializers.GenderDetail.name),
    url(r'^size-list/$', views_serializers.SizeList.as_view(), name=views_serializers.SizeList.name),
    url(r'^size-list/(?P<pk>[0-9]+)$', views_serializers.SizeDetail.as_view(), name=views_serializers.SizeDetail.name),
    url(r'^firms-list/$', views_serializers.FirmsList.as_view(), name=views_serializers.FirmsList.name),
    url(r'^firms-list/(?P<pk>[0-9]+)$', views_serializers.FirmsDetail.as_view(), name=views_serializers.FirmsDetail.name),
    url(r'^subcategory-list/$', views_serializers.SubCategoryList.as_view(), name=views_serializers.SubCategoryList.name),
    url(r'^subcategory-list/(?P<pk>[0-9]+)$', views_serializers.SubCategoryDetail.as_view(), name=views_serializers.SubCategoryDetail.name),
    url(r'^news-list/$', views_serializers.NewsList.as_view(), name=views_serializers.NewsList.name),
    url(r'^news-list/(?P<pk>[0-9]+)$', views_serializers.NewsDetail.as_view(), name=views_serializers.NewsDetail.name),
    url(r'^message-list/$', views_serializers.MessageList.as_view(), name=views_serializers.MessageList.name),
    url(r'^message-list/(?P<pk>[0-9]+)$', views_serializers.MessageDetail.as_view(), name=views_serializers.MessageDetail.name),
    url(r'^address-list/$', views_serializers.AddressList.as_view(), name=views_serializers.AddressList.name),
    url(r'^address-list/(?P<pk>[0-9]+)$', views_serializers.AddressDetail.as_view(), name=views_serializers.AddressDetail.name),
    url(r'^category-list/$', views_serializers.CategoryList.as_view(), name=views_serializers.CategoryList.name),
    url(r'^category-list/(?P<pk>[0-9]+)$', views_serializers.CategoryDetail.as_view(), name=views_serializers.CategoryDetail.name),
    url(r'^user-list/$', views_serializers.UserList.as_view(), name=views_serializers.UserList.name),
    url(r'^user-list/(?P<pk>[0-9]+)$', views_serializers.UserDetail.as_view(), name=views_serializers.UserDetail.name),

    url(r'^$', views_serializers.ApiRoot.as_view(), name=views_serializers.ApiRoot.name)
]