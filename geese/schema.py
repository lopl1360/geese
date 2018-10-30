import graphene

from geese.models import URL
from graphene import ObjectType, Node, Schema, relay
from graphene_django.fields import DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphene import InputObjectType
from geese.helpers import get_object, get_errors, update_create_instance

class URLNode(DjangoObjectType):

    class Meta:
        model = URL
	filter_fields = {
            'id': ['exact']
            }

        interfaces = (relay.Node, )

class UrlCreateInput(InputObjectType):
	url = graphene.String(required=True)
	short = graphene.String(required=True)
	count = graphene.Int(required=False)

#class CreateUrl(graphene.Mutation):
#     class Arguments:
#	url = graphene.String(required=True)
#	short = graphene.String(required=True)
#	count = graphene.Int(required=False)
#
#    result = graphene.Boolean()
#    url = graphene.Field(lambda: URL)
#
#    def mutate(self, info, url):
#        url = URL(url=url)
#        result = True
#        return CreateUrl(url=url, result=result)

class CreateUrl(relay.ClientIDMutation):
  
    class Arguments:
        url = graphene.Argument(UrlCreateInput)

    new_url = graphene.Field(URLNode)

    @classmethod
    def mutate_and_get_payload(cls, args, context, info):

        url_data = args.get('url') # get the url input from the args
        url = URL() # get an instance of the URL  model here
        new_url = update_create_instance(url, url_data) # use custom function to create url

        return cls(new_url=new_url) # newly created url instance returned.

class Query(ObjectType):
        all_urls = graphene.List(URLNode)
	urls = DjangoFilterConnectionField(URLNode)

	def resolve_all_urls(self, args):
	    return URL.objects.all()

class Mutation(ObjectType):
     create_url = CreateUrl.Field()
	

schema = graphene.Schema(query=Query, mutation=Mutation)
