from django.urls import path

from .views import base_views, question_views, answer_views, category_veiws, notice_views

app_name = 'passcode'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    # path('<int:question_id>/',
    #      base_views.detail, name='detail'),

    # main 관련
    path('index/',
         category_veiws.index, name='index'),
    # About PASSCODE
    path('company_info/',
         category_veiws.company_info, name='company_info'),
    path('service/',
         category_veiws.service_info, name='service_info'),
    path('partners_info/',
         category_veiws.partners_info, name='partners_info'),
    # Digital Assets
    path('cryptocurrency_info/',
         category_veiws.cryptocurrency_info, name='cryptocurrency_info'),

    path('ntf_info/',
         category_veiws.nft_info, name='nft_info'),

    # 공지사항
    path('notice_list/',
         notice_views.notice_list, name='notice_list'),
    path('notice/<int:notice_id>/', notice_views.notice_detail, name='notice_detail'),

    # 뉴스
    path('news_board/',
         category_veiws.news_board, name='news_board'),
    # Contact Us
    path('contact_us/',
         category_veiws.contact_us, name='contact_us'),


    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/',
         question_views.question_vote, name='question_vote'),


    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/',
         answer_views.answer_vote, name='answer_vote'),
]