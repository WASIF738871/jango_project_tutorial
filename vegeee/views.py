from django.shortcuts import render, redirect
from vegeee.models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def login_page(request):
     
    return render(request, 'login.html')

def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = User.objects.filter(username= username)

        if user.exists():
            messages.info(request, "User already registered")
            return render(request, 'register.html')

        user= User.objects.create(
            
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()


    messages.info(request, "User registered Successfully") 
    return render(request, 'register.html')


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

    if request.GET.get('search'):
        print(request.GET.get('search'))
        all_recipe = all_recipe.filter(title__icontains = request.GET.get('search') )

    context = {
        "all_recipe":all_recipe
    }
    # print(context)
     
    return render(request, 'table.html', context)



def deleteRecipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/render-table/')



def updateRecipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.POST:
        data = request.POST
        queryset.title= data.get('title')
        queryset.description= data.get('description')
        queryset.recipe_image = request.FILES.get('recipe_image')
        queryset.save()
        return redirect('/render-table')
    
    context ={"recipe":queryset}
    return render(request, 'recipeupdateform.html', context)
