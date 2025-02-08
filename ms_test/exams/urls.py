from django.urls import path
from .views import *

urlpatterns = [
    path('subjects/', CreateSubjectView.as_view(), name='create_subject'),
    path('subjects/list/', ListSubjectsView.as_view(), name='list_subjects'),  # Add the new URL pattern
    path('questions/', CreateQuestionWithAnswersView.as_view(), name='create_question_with_answers'),
    path('question-pools/', CreateQuestionPoolView.as_view(), name='create_question_pool'),
    path('generate-test/', GenerateTestView.as_view(), name='generate_test'),
    path('regenerate-test/<int:test_id>/', RegenerateTestFileView.as_view(), name='regenerate_test_file'),
    path('download-word/<int:test_id>/', download_word_file, name='download_word_file'),
    path('tests/<str:assessment_id>/correct_answers/', correct_answers_view, name='correct_answers'),
]