from rest_framework import serializers
from .models import TreeNode


class TreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = TreeNode
        fields = ('id', 'name', 'children')

    def get_children(self, obj):
        return TreeSerializer(obj.get_children(), many=True, required=False).data
