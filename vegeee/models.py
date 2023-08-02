from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    recipe_image = models.ImageField(upload_to='uploads')
    # prep_time = models.PositiveIntegerField()
    # cook_time = models.PositiveIntegerField()
    # total_time = models.PositiveIntegerField()
    # servings = models.PositiveIntegerField()
    # Add more fields as needed (e.g., author, image, cuisine type, etc.)

    def __str__(self):
        return self.title
