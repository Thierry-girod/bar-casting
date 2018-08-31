from models.persitence.recipe import Recipe, db
from models.persitence.recipe_product import RecipeProduct

def find_by(etablishment_id, *args, order_by='name', **kwargs):
    return Recipe.find_by(
        *args,
        etablishment_id=etablishment_id,
        order_by=order_by,
        deleted_at=None,
        **kwargs
    )

def list_recipe_with_volume_and_nb_product(etablishment_id, order_by='name'):
    return Recipe.list_recipe_with_volume_and_nb_product(etablishment_id, order_by)

def create(*args, product_quantity, **kwargs):
    recipe = Recipe(**kwargs)
    recipe.save()
    print(recipe.id)

    for product_id, quantity in product_quantity.items():
        reci_prod = RecipeProduct(
            product_id=product_id,
            quantity=quantity,
            recipe_id=recipe.id
        )
        reci_prod.save()

    return recipe




def delete(id):
    RecipeProduct.delete_recipe(id)
    # RecipeProduct.find_by(product_id=id).delete()
    return Recipe.delete(id)
