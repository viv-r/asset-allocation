"""
This file contains test cases for the functions
defined in the frontend folder. Tests for all the modules
have been included in the same file.

Classes:
    UnitTests: Class containing  all the test cases
Functions:
    Different types of unittest cases.
Exceptions:
    None.
"""
#pylint: enable=duplicate-code
import sys
import os
import inspect
import unittest

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
FINAL_DIR = os.path.join(str(PARENT_DIR), "assetallocation")
sys.path.insert(0, PARENT_DIR)
sys.path.insert(0, FINAL_DIR)
#pylint: disable=duplicate-code
#pylint: disable=wrong-import-position
from frontend import introduction_tab
#pylint: enable=wrong-import-position

class UnitTests(unittest.TestCase):
    """Set of unittests for the frontend folder.

    Each function in this class is a self contained unittest.
    All queries necessary for execution are run inside the functions
    without using any global results or variables.
    """

    def test_intro_tab_return(self):
        """check if into tab returns a markdown doc as
        expected.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected return type encountered.

        Raises:
            Raises AssertionError: Type not equal
        """
        df_to_test = introduction_tab.get_component()
        self.assertEqual(str(type(df_to_test)), "<class 'Markdown'>")

    def test_attach_callback_return(self):
        """check if into tab returns a markdown doc as
        expected.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected return type encountered.

        Raises:
            Raises AssertionError: Type not equal
        """
        test_var = "_app"
        # pylint: disable = assignment-from-no-return
        df_to_test = introduction_tab.attach_callbacks(test_var)
        # pylint: enable = assignment-from-no-return
        self.assertEqual(df_to_test, None)

SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(SUITE)
