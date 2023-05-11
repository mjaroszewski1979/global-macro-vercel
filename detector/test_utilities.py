import unittest
from unittest.mock import patch
from utilities import get_result, get_score

class TestUtilities(unittest.TestCase):

    def test_get_result(self):
        fake_response = [[{'level1' : 100}], [{'level2' : 200}]]

        with patch('detector.utilities.get_result.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_response

            response = get_result('i like you. i love you.')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_response)

if __name__ == '__main__':
    unittest.main()