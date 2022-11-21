from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class TreeNode(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, related_name='child')

    def __str__(self):
        return "<TreeNode: {} {}>".format(self.name)

    def __repr__(self):
        return self.__str__()
