from django.db import models

class Subject(models.Model):
    institution_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()  # This should reference the user_id from UserService
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class QuestionPool(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='question_pools')
    instructor_id = models.IntegerField()  # Referenced via user_id from UserService
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_pool = models.ForeignKey(QuestionPool, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    default_score = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']  # Ensure consistent ordering when retrieving answers

    def __str__(self):
        return self.text[:50]

class Test(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tests')
    instructor_id = models.IntegerField()  # Referenced via user_id from UserService
    assessment_id = models.CharField(max_length=6, unique=True)  # Randomly generated 5-digit string
    name = models.CharField(max_length=255)
    variant = models.CharField(max_length=2)
    notes = models.CharField(max_length=255, blank=True, null=True)
    instructions = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (Variant {self.variant})"

class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_questions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    position = models.IntegerField()  # Added field to store the order/position of the question
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Test {self.test.id} - Q{self.position}"

class GeneratedTestLink(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='generated_links')
    exam_file = models.BinaryField()  # Generated Word file as bytes
    created_at = models.DateTimeField(auto_now_add=True)