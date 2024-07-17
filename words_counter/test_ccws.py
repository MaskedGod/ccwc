import subprocess
import unittest


class TestWordCounter(unittest.TestCase):

    def test_byte_count(self):
        process = subprocess.run('py ccwc.py -b test.txt', shell=True, capture_output=True, text=True)
        self.assertEqual(process.stdout.strip("\n"), "342190")

    def test_line_count(self):
        process = subprocess.run('py ccwc.py -l test.txt', shell=True, capture_output=True, text=True)
        self.assertEqual(process.stdout.strip("\n"), "7145")

    def test_word_count(self):
        process = subprocess.run('py ccwc.py -w test.txt', shell=True, capture_output=True, text=True)
        self.assertEqual(process.stdout.strip("\n"), "58164")

    def test_characters_count(self):
        process = subprocess.run('py ccwc.py -c test.txt', shell=True, capture_output=True, text=True)
        self.assertEqual(process.stdout.strip("\n"), "332147")

    def test_default_option(self):
        process = subprocess.run('py ccwc.py test.txt', shell=True, capture_output=True, text=True)
        self.assertEqual(process.stdout.strip("\n"), "7145 58164 342190")

    def test_standard_input(self):
        process = subprocess.run('py ccwc.py -l', input='test.txt', shell=True, capture_output=True, text=True)
        self.assertEqual(process.stdout.strip("\n"), "7145")


if __name__ == '__main__':
    unittest.main()