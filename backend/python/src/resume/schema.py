import graphene
from graphene_django import DjangoObjectType

from .models import Profile, Experience

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile

class ExperienceType(DjangoObjectType):
    class Meta:
        model = Experience

class Query(graphene.ObjectType):
    profiles=graphene.List(ProfileType)
    def resolve_profiles(self, info, **kwargs):
        return Profile.objects.all()

    experiences=graphene.List(ExperienceType)
    def resolve_experiences(self, info, **kwargs):
        return Experience.objects.all()

# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)