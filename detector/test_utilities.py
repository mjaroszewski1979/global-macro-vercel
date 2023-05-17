import unittest
from django.test import TestCase
from .utilities import get_score

class TestUtilities(TestCase):
    """
    A test case class for testing the utilities module.

    """


    def test_get_score_error(self):
        """
        Test case to verify the behavior of `get_score` when an error occurs.

        """
        data = {}
        result = get_score(data)

        self.assertEqual(result, "Error")

    def test_get_score_label0_gt_label1(self):
        """
        Test case to verify the behavior of `get_score` when label 0 has a greater score than label 1.

        """
        data = [[{'label': 'LABEL_0', 'score': 0.8824092149734497},
                {'label': 'LABEL_1', 'score': 0.11759082227945328}]]
        result = get_score(data)

        self.assertEqual(result, False)

    def test_get_score_label0_lt_label1(self):
        """
        Test case to verify the behavior of `get_score` when label 0 has a lower score than label 1.
        
        """
        data = [[{'label': 'LABEL_0', 'score': 0.1824092149734497},
                {'label': 'LABEL_1', 'score': 0.81759082227945328}]]
        result = get_score(data)

        self.assertEqual(result, True)

   


    



if __name__ == '__main__':
    unittest.main()