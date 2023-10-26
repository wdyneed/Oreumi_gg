from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'gg_app' 
 
urlpatterns = [
    path('', views.index, name='index'),
    path('modes/', views.modes, name='modes'),


    # 통계
    path('statistics_champions/', views.statistics_champions, name='statistics_champions'),
    path('statistics_tier/', views.statistics_tier, name='statistics_tier'),

    # 랭킹
    path('leaderboards/', views.leaderboards, name='leaderboards'),
    path('type_champions/', views.type_champions, name='type_champions'),
    path('type_ladder_flex/', views.type_ladder_flex, name='type_ladder_flex'),
    path('type_ladder/', views.type_ladder, name='type_ladder'),
    path('type_level/', views.type_level, name='type_level'),

    #커뮤니티, 글 작성
    path('community/', views.community, name='community'),
    path('post/', views.post, name='post'),
    path('write/', views.post_write, name='post_write'), 
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),      # 새로 추가한 URL 패턴), <int:post_id> 부분은 URL 패턴에서 변수를 캡처하는 부분
    path('post_edit/<int:post_id>/', views.post_edit, name='post_edit'),     # post_edit 수정 부분

    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('posts/<str:order_by>/', views.post_list, name='post_list'),

    #챔피언 티어 및 로테이션 정보
    path('champions/', views.champions, name='champions'),
    path('champions/champions_tier/<str:position>/<str:region>/<str:tier>', views.champion_tier_list, name='champion_tier'),
    path('champions/lotation/', views.lotation_list, name='lotation'),
    
    #인게임 정보
    path('ingame/', views.ingame_info, name='ingame'),
    
    # 전적 검색
    path('summoners_form', views.summoners_info_form, name='summoners_info_form'),
    path('summoners/<str:country>/<str:summoner_name>', views.summoners_info, name='summoners_info'),   #검색결과를 보여줄 화면
    path('api/summoners_info/<str:country>/<str:summoner_name>/<int:count>/<int:queue>', views.summoners_info_api, name='summoners_info_api'),
]
