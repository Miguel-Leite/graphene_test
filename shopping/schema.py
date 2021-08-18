import graphene
from graphene.types import schema
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

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_categorys = graphene.List(CategoryType)

    def resolve_all_products(self, info):
        return Product.objects.all()

    def resolve_all_category(self, info):
        return Category.objects.all()
