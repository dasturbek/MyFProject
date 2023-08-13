from rest_framework import serializers
from home.models import PostCommentsModel, PostModel
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_fields = ['url']
        fields = '__all__'
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return  self.Meta.extra_fields + expanded_fields
        else:
            return expanded_fields

class PostModelSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    class Meta:
        model = PostModel
        extra_fields = ['url']
        fields = '__all__'
        # read_only_fields = ('summury','author')
        write_only_fields = ('author', 'summury')
    # def get_field_names(self, declared_fields, info):
    #     expanded_fields = super().get_field_names(declared_fields, info)

    #     if getattr(self.Meta, 'extra_fields', None):
    #         return  self.Meta.extra_fields + expanded_fields
    #     else:
    #         return expanded_fields
        