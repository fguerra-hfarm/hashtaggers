import os
import unittest
from use_csv_package import posts_csv
# to run it: python3 -m unittest use_csv_package/tests/test_posts_csv.py


class TestFile(unittest.TestCase):
    """Unit testing framework - Using a specific .csv file

    Checking code validity with the unittest development tool.
    Used in this case to test scenarios regarding the use of a .csv file,
    which might not exists in the directory and/or it is empty.
    """

    # setUp function prepare some data for tests
    def setUp(self):
        # create an empty file
        # note: this would be better done with temporary file
        self.temporary_file = os.path.dirname(
            os.path.abspath(__file__)) + '/data/empty_file.csv'
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        d = posts_csv.use_post_csv('/tmp/nonexistentfile-wewefwwe')
        self.assertFalse(d)

    def test_empty_datafile(self):
        d = posts_csv.use_post_csv(self.temporary_file)
        self.assertFalse(d)

    # tearDown function cleans the temporary data
    def tearDown(self):
        os.remove(self.temporary_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
