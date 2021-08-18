import graphene
import shopping.schema

class Query(shopping.schema.Query, graphene.ObjectType):
    pass

class Mutation(shopping.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)