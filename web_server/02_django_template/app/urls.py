from django.urls import path  # URL 경로를 설정하는 함수
from . import views           # 현재 앱의 views 모듈

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),  # /app/ 요청을 index 뷰와 연결
    # /first/01_variables_filters 요청을 _01_variables_filters 뷰와 연결
    path('01_variables_filters', views._01_variables_filters, name='01_variables_filters'),
    path('02_tags', views._02_tags, name='02_tags'),
    path('03_layout', views._03_layout, name='03_layout'),
    path('04_static_files', views._04_static_files, name='04_static_files'),
    path('05_urls', views._05_urls, name='05_urls'),
    path('articles_detail/<int:id>', views.articles_detail, name='articles_detail'),
    path('articles_category/<str:category>/<int:id>', views.articles_category, name='articles_category'),
    path('search', views.search, name='search'),
    path('06_bootstrap', views._06_bootstrap, name='06_bootstrap'),
    path('06_my_bootstrap', views._06_my_bootstrap, name='06_my_bootstrap'),
]