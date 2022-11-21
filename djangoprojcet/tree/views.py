from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import TreeNode
from .serializers import TreeSerializer
from mptt.models import MPTTModel, TreeForeignKey


class TreeView(ListAPIView):
    serializer_class = TreeSerializer
    queryset = TreeNode.objects.filter(level=0)


class TestView(RetrieveAPIView):

    def createFiveLevelsScenario(self):
        parent_obj = None
        for level in range(1, 5):
            if parent_obj is None:
                parent_name = "nest_five_" + str(level)
                parent_obj = TreeNode.objects.create(
                    name=parent_name)
                continue
            child_name = "nest_child_five_" + str(level)
            child_obj = TreeNode.objects.create(name=child_name,
                                                parent=parent_obj)
            parent_obj = child_obj

    def createFiveHundredLevelsScenario(self):
        parent_obj = None
        for level in range(1, 50):
            if parent_obj is None:
                parent_name = "nest_five_hundred_" + str(level)
                parent_obj = TreeNode.objects.create(
                    name=parent_name)
                continue
            child_name = "nest_child_five_hundred_" + str(level)
            child_obj = TreeNode.objects.create(name=child_name,
                                                parent=parent_obj)
            parent_obj = child_obj

    def get(self, request, **kwargs):
        self.createFiveLevelsScenario()
        self.createFiveHundredLevelsScenario()


