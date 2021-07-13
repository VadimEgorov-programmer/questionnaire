from django.db import models


class Poll(models.Model):
    poll_name = models.CharField(max_length=100, verbose_name='Name')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Start date')
    end_date = models.DateTimeField(verbose_name='End date')
    poll_description = models.CharField(max_length=200, verbose_name='Description')

    def __str__(self):
        return self.poll_name


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    text_question = models.CharField(max_length=200)
    type_question = models.CharField(max_length=200, verbose_name='type question')

    def __str__(self):
        return self.text_question


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, related_name='Poll', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.choice_text