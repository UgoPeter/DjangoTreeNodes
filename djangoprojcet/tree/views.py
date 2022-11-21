from rest_framework.generics import ListAPIView
from .models import TreeNode
from .serializers import TreeSerializer


class TreeView(ListAPIView):
    serializer_class = TreeSerializer
    queryset = TreeNode.objects.filter(level=0)
