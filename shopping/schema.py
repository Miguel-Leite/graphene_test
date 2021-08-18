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

class ProductInput(graphene.InputObjectType):
    id = graphene.ID()
    product = graphene.String()
    category = graphene.String()
    price = graphene.Float()
    description = graphene.String()


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

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_categorys = graphene.List(CategoryType)

    def resolve_all_products(self, info):
        return Product.objects.all()

    def resolve_all_category(self, info):
        return Category.objects.all()


class Mutation(graphene.ObjectType):
    addProduct = AddProduct.Field()