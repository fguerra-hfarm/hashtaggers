import unittest
from hashtagify_package import api_hashtagify
# run: python3 -m unittest hashtagify_package/tests/test_api_hashtagify.py


class TestInputHashtagify(unittest.TestCase):
    """Unit testing framework - API Queries

    Checking code validity with the unittest development tool.
    Used to test input values to know valid/invalid entries,
    and edge/boundary/corner cases of the tested function.
    """

    # smoke test: valid inputs
    def test_correct_values(self):
        self.assertEqual(api_hashtagify.get_insights(
                        vot='c', hashtag='test'), None)

    # invalid inputs
    def test_wrong_values(self):
        # input wrong data
        self.assertEqual(api_hashtagify.get_insights('$'), None)
        self.assertEqual(api_hashtagify.get_insights('£'), None)
        self.assertEqual(api_hashtagify.get_insights('\t'), None)
        self.assertEqual(api_hashtagify.get_insights('\n'), None)
        self.assertEqual(api_hashtagify.get_insights('\\'), None)
        self.assertEqual(api_hashtagify.get_insights(' '), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(api_hashtagify.get_insights(''), None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
