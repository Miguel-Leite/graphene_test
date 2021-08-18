import graphene
from graphene_django import DjangoObjectType
from .models import Category, Product 

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ['id','product', 'category', 'price', 'description']

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ['id','category']

# ----------------------------------------------------------------
# Seting data product
class ProductInput(graphene.InputObjectType):
    id = graphene.ID()
    product = graphene.String()
    category = graphene.Int()
    price = graphene.Float()
    description = graphene.String()

# ----------------------------------------------------------------
# Create new product
class AddProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)
    
    product = graphene.Field(ProductType)

    def mutate(self, info, product_data=None):
        product_instance = Product(
            product=product_data.product,
            category=product_data.category,
            price=product_data.price,
            description=product_data.description
        )
        product_instance.save()
        return AddProduct(product=product_instance)

# ----------------------------------------------------------------
# seting data category
class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    category = graphene.String()

# ----------------------------------------------------------------
# Create new category
class AddCategory(graphene.Mutation):
    class Arguments:
        category_data = CategoryInput(required=True)
    
    category = graphene.Field(CategoryType)

    def mutate(self, info, category_data=None):
        category_instance = Category(
            category=category_data.category
        )
        category_instance.save()
        return AddCategory(category=category_instance)

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_categorys = graphene.List(CategoryType)

    def resolve_all_products(self, info):
        return Product.objects.all()

    def resolve_all_category(self, info):
        return Category.objects.all()

# ----------------------------------------------------------------
# Update category
class UpdateCategory(graphene.Mutation):
    class Arguments:
        category_data = CategoryInput(required=True)
    
    category = graphene.Field(CategoryType)

    def mutate(self, info, category_data=None):

        category_instance = Category.objects.get(pk=category_data.id)

        if category_instance:
            category_instance.category = category_data.category
            category_instance.save()
            return UpdateCategory(category=category_instance)

        return UpdateCategory(category=None)

# ----------------------------------------------------------------
# Delete category
class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    def mutate(self, info, id):
        category_instance = Category.objects.get(pk=id)
        category_instance.delete()

        return None


# ----------------------------------------------------------------
# Mutation
class Mutation(graphene.ObjectType):
    addProduct = AddProduct.Field()

    # Mutation Category
    addCategory = AddCategory.Field()
    updateCategory = UpdateCategory.Field()
    deleteCategory = DeleteCategory.Field()