from django.urls import path
from .views import *

urlpatterns = [
    path('subjects/', CreateSubjectView.as_view(), name='create_subject'),
    path('subjects/list/', ListSubjectsView.as_view(), name='list_subjects'),
    path('subjects/<int:pk>/', RetrieveSubjectView.as_view(), name='retrieve_subject'),
    path('questions/', CreateQuestionWithAnswersView.as_view(), name='create_question_with_answers'),
    path('questions/question-pool/<int:question_pool_id>/', ListQuestionsByQuestionPoolView.as_view(), name='list_questions_by_question_pool'),
    path('question-pools/', CreateQuestionPoolView.as_view(), name='create_question_pool'),
    path('question-pools/subject/<int:subject_id>/', ListQuestionPoolsBySubjectView.as_view(), name='list_question_pools_by_subject'),
    path('generate-test/', GenerateTestView.as_view(), name='generate_test'),
    path('tests/subject/<int:subject_id>/', ListTestsBySubjectView.as_view(), name='list_tests_by_subject'),
    path('tests/<str:assessment_id>/', RetrieveTestByAssessmentIdView.as_view(), name='retrieve_test_by_assessment_id'),
    path('tests/<str:assessment_id>/questions/', ListTestQuestionsByAssessmentIdView.as_view(), name='list_test_questions_by_assessment_id'),  # New URL pattern
    path('tests/subject/<int:subject_id>/group-ids/', ListGroupIdsBySubjectView.as_view(), name='list_group_ids_by_subject'),
    path('tests/group/<str:group_id>/', ListTestsByGroupIdView.as_view(), name='list_tests_by_group_id'),
    path('tests/group/<str:group_id>/download-link/', GetDownloadLinkByGroupIdView.as_view(), name='get_download_link_by_group_id'),  # Updated URL pattern
    path('regenerate-test/<int:test_id>/', RegenerateTestFileView.as_view(), name='regenerate_test_file'),
    path('download-word/<int:test_id>/', download_word_file, name='download_word_file'),
    path('tests/<str:assessment_id>/correct_answers/', correct_answers_view, name='correct_answers'),
    path('questions/bulk/<int:question_pool>/', CreateManyQuestionsView.as_view(), name='create_many_questions'),
    path('questions/question-pool/<int:question_pool>/delete/<int:id>/', DeleteQuestionFromPoolView.as_view(), name='delete_question_from_pool'),
]