from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete, ResponseList, ResponseCreate, ResponseUpdate, ResponseDelete, ResponseDetail


urlpatterns = [
path('', (ArticleList.as_view()), name='article_list'),
path('<int:id>', (ArticleDetail.as_view()), name='article_detail'),
path('create/', ArticleCreate.as_view(), name='article_create'),
path('<int:id>/update/', ArticleUpdate.as_view(), name='article_update'),
path('<int:id>/delete/', ArticleDelete.as_view(), name='article_delete'),
path('response/', (ResponseList.as_view()), name='response_list'),
path('response/<int:id>', (ResponseDetail.as_view()), name='response_detail'),
path('response/create/', ResponseCreate.as_view(), name='response_create'),
path('response/<int:id>/update/', ResponseUpdate.as_view(), name='response_update'),
path('response/<int:id>/delete/', ResponseDelete.as_view(), name='response_delete'),
]





