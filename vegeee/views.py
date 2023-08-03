from django.shortcuts import render
from vegeee.models import Recipe

# Create your views here.
def recipeform(request):
     
    if(request.POST):
        data = request.POST
        title= data.get('title')
        description= data.get('description')
        recipe_image = request.FILES.get('recipe_image')
        print(recipe_image)    
        print(data)
        Recipe.objects.create(
            title= title, 
            description= description,
            recipe_image= recipe_image
            )
        
        
    return render(request, 'recipeform.html')


def recipeTable(request):

    all_recipe = Recipe.objects.all()

    context = {
        "all_recipe":all_recipe
    }
    print(context)
     
    return render(request, 'table.html', context)
