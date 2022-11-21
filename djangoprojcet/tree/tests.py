import json
from django.test import TransactionTestCase
from .models import TreeNode
from rest_framework.test import APIRequestFactory
from .test import test_data
from .views import TreeView


class Tests(TransactionTestCase):
    reset_sequences = True

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

    def testFiveLevelScenario(self):
        test_file = test_data.five_level_scenario
        view = TreeView.as_view()
        factory = APIRequestFactory()
        request = factory.get('/tree/')
        response = json.dumps(view(request).data[0])
        self.assertJSONEqual(response, test_file)

    def testFiftyLevelScenario(self):
        test_file = test_data.fifty_level_scenario
        view = TreeView.as_view()
        factory = APIRequestFactory()
        request = factory.get('/tree/')
        response = json.dumps(view(request).data[1])
        self.assertJSONEqual(response, test_file)

    def testAllScenario(self):
        test_file = test_data.all_level_scenario
        view = TreeView.as_view()
        factory = APIRequestFactory()
        request = factory.get('/tree/')
        response = json.dumps(view(request).data)
        self.assertJSONEqual(response, test_file)

    def setUp(self):
        self.createFiveLevelsScenario()
        self.createFiveHundredLevelsScenario()
