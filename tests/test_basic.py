# -*- coding: utf-8 -*-

from .context import assessment_package

import unittest
import pandas as pd
import numpy as np
from numpy.testing import assert_array_equal

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


class DFTests(unittest.TestCase):

    """ class for running unittests """

    def setUp(self):
        """ Your setUp """
        TEST_INPUT_DIR = 'data/'
        test_file_name =  'testdata.csv'
        try:
            data = pd.read_csv(TEST_INPUT_DIR + test_file_name,
                sep = '\t',
                header = 0)
        except IOError:
            print('cannot open file')
        self.fixture = data

    def test_count_sig(self):
        """ test count sig fuction """
        self.assertEqual(assessment_package.count_sig(self.fixture), 0)

    def test_palindrom_detection(self):
        """ test detect_palindromic """
        self.assertEqual(sum(assessment_package.helpers.detect_palindromic(self.fixture)), 10)

    def test_detect_within_thresh(self):
        """ test within thresh """
        bool = [True, False, True, True, True, False, False, True, False, True, False, False, False, False, False]
        assert_array_equal(assessment_package.helpers.detect_within_thresh(self.fixture, 0.05), bool)
        self.assertEqual(sum(assessment_package.helpers.detect_within_thresh(self.fixture, 0.1)), 8)

    def test_remove_palidromic_thresh(self):
        """ test remove palindromic vars withhin thresh """
        self.assertEqual(len(assessment_package.remove_palidromic_thresh(self.fixture, 0.2)), 5)
        self.assertEqual(len(assessment_package.remove_palidromic_thresh(self.fixture, 0.1)), 7)
        self.assertEqual(len(assessment_package.remove_palidromic_thresh(self.fixture, 0.05)), 9)

if __name__ == '__main__':
    unittest.main()
