from rest_framework import serializers
from .models import Subject, QuestionPool, Question, Answer

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'institution_id', 'name', 'description', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class QuestionPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPool
        fields = ['id', 'subject', 'instructor_id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_pool', 'text', 'default_score', 'answers', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)
        return question

# -------------------------------
# Serializers for test generation
# -------------------------------

class TestGenerationQuestionSelectionSerializer(serializers.Serializer):
    question_pool = serializers.IntegerField()
    positions = serializers.ListField(child=serializers.IntegerField(), allow_empty=False)

class TestGenerationSerializer(serializers.Serializer):
    subject = serializers.IntegerField()
    instructor_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    # Variants for the test (e.g., ["A", "B"]).
    # The first variant will use the positions as given; additional ones will have shuffled orders.
    variants = serializers.ListField(child=serializers.CharField(max_length=2))
    # List of question selections – each entry determines from which question pool to randomly
    # select questions and the positions in the test exam where they should appear.
    question_selections = TestGenerationQuestionSelectionSerializer(many=True)
