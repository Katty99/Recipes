from django.shortcuts import render

from Recipes.recipe.models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, template_name='common/index.html', context=context)
