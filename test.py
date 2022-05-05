import unittest
from unittest import mock
import python_technical_test

class TestETL(unittest.TestCase):
    def testTransformation_1(self):
        result = python_technical_test.transformation_1("hello world")
        self.assertEqual(result, "HELLO WORLD")

    def testTransformation_2(self):
        result = python_technical_test.transformation_2("Hello world, hello")
        self.assertDictEqual(result, {'hello':2, 'world':1})

    def testExtract_from_file(self):
        result = python_technical_test.extract("input.txt")
        self.assertEqual(result, "hello world, Hello")

    def testLoad(self):
        open_mock = mock.mock_open()
        with mock.patch("python_technical_test.open", open_mock, create=True):
            python_technical_test.load("test-data", "output.txt")

        open_mock.assert_called_with("output.txt", "w")
        open_mock.return_value.write.assert_called_once_with("test-data")

if __name__ == '__main__':
    unittest.main()