from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import TreeNode
from .serializers import TreeSerializer
from mptt.models import MPTTModel, TreeForeignKey


class TreeView(ListAPIView):
    serializer_class = TreeSerializer
    queryset = TreeNode.objects.filter(level=0)
