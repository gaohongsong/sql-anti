from django.db import models

# Create your models here.

class Food(models.Model):
	title = models.CharField(max_length=50)
	parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

	def __unicode__(self):
		return self.title

	@classmethod
	def init_test_data(cls):
		food = cls.objects.create(title="Food")

		fruit = cls.objects.create(title="Fruit", parent=food)

		red = cls.objects.create(title="Red", parent=fruit)
		cherry = cls.objects.create(title="Cherry", parent=red)

		yellow = cls.objects.create(title="Yellow", parent=fruit)
		banana = cls.objects.create(title="Banana", parent=yellow)

		meat = cls.objects.create(title="Meat", parent=food)

		beef = cls.objects.create(title="Beef", parent=meat)
		pork = cls.objects.create(title="Pork", parent=meat)
