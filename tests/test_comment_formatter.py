import os
import unittest

from comment_formatter.formatter import rewrite_comments


EXAMPLE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")


class FormatterTest(unittest.TestCase):
    def test_examples(self):
        """Test all the examples in the examples directory"""
        example_files = os.listdir(EXAMPLE_DIR)
        input_files = [x for x in example_files if x.startswith("input_")]

        for input_file_name in input_files:
            example_index = input_file_name.strip(".py").split("_")[-1]
            output_file_name = "output_" + example_index + ".py"
            full_input_path = os.path.join(EXAMPLE_DIR, input_file_name)
            full_output_path = os.path.join(EXAMPLE_DIR, output_file_name)

            with open(full_input_path) as f:
                input_text = f.read()

            with open(full_output_path) as f:
                expected_output_text = f.read()

            output_text = rewrite_comments(input_text, max_line_length=100)
            self.assertEqual(output_text, expected_output_text)

            print("succeeded on", input_file_name)
        self.fail()
