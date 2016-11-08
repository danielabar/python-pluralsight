import unittest
import os


# In a real app, this production code would be in a separate file from the test code, and imported into the test file.
def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If ``filename`` does not exist or can't be read.

    Returns:
        The number of lines in the file.
    """
    with open(filename, 'r') as f:
        return sum(1 for _ in f)


# Create test case by creating a class which derives from unittest.TestCase
class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that runs before each test method. It creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Nowwe are engated in a great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')

    def tearDown(self):
        """Fixture that runs after each test method. It deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            # swallow exceptions because cannot be certain that file exists
            pass

    # Define test methods by naming them starting with test_
    # These are automatically discovered by unittest framework
    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        # Test will fail if any exceptions are thrown, for example if method is not defined
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename), 4)


if __name__ == '__main__':
    # Searches for all TestCase subclasses in a module and execute all of their methods.
    unittest.main()
