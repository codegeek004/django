from django.db import models
#####for multiple inheritence#####
class Quiz(models.Model):
	name = models.CharField(max_length=256)

	def __str__(self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(
		Quiz,
		on_delete=models.CASCADE,
		related_name='%(class)s'
		)
	text = models.CharField(max_length=1000)
	order = models.SmallIntegerField()
	class Meta:
		ordering = ('order',)
	def __str__(self):
		return self.text


class MCQuestion(Question):
	number_of_answers = models.PositiveSmallIntegerField()

class BooleanQuestion(Question):
	is_true = models.BooleanField()


######for abstract inheritence########
# class Quiz(models.Model):
# 	name = models.CharField(max_length=256)

# 	def __str__(self):
# 		return self.name

# class Question(models.Model):
# 	quiz = models.ForeignKey(
# 		Quiz,
# 		on_delete=models.CASCADE,
# 		related_name='%(class)s'
# 		)
# 	text = models.CharField(max_length=1000)
# 	order = models.SmallIntegerField()
# 	class Meta:
# 		ordering = ('order',)
# 		abstract=True
# 	def __str__(self):
# 		return self.text


# class MCQuestion(Question):
# 	number_of_answers = models.PositiveSmallIntegerField()

# class BooleanQuestion(Question):
# 	is_true = models.BooleanField()