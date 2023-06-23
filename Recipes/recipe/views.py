from django.shortcuts import render, redirect

from Recipes.recipe.forms import RecipeForm, DeleteRecipeForm
from Recipes.recipe.models import Recipe


# Create your views here.
def create_recipe(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, template_name='recipe/create.html', context=context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == "GET":
        form = RecipeForm(initial=recipe.__dict__)
        context = {'form': form}
        return render(request, template_name='recipe/edit.html', context=context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {'form': form}
            return render(request, template_name='recipe/edit.html', context=context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    if request.method == "POST":
        recipe.delete()
        return redirect('home')

    form = DeleteRecipeForm(instance=recipe)
    context = {'form': form}
    return render(request, template_name='recipe/delete.html', context=context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {'recipe': recipe}
    return render(request, template_name='recipe/details.html', context=context)
