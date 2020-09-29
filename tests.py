import unittest

import magic

import detector
from exceptions import *


class SeeMimeTypes(unittest.TestCase):
    def setUp(self) -> None:
        self.mime = magic.Magic(mime=True)
        
    def test_sucesses(self):
        detector.detect_true_type("tests_folder/true_image.jpg")
        detector.detect_true_type("tests_folder/true_image.pdf")
        detector.detect_true_type("tests_folder/true_pdf.jpg")
        detector.detect_true_type("tests_folder/true_pdf.pdf")
        detector.detect_true_type("tests_folder/encoding_utf8.txt")
    
    def test_raises(self):
        files = [
            "tests_folder/manipulated_from_pdf.jpg",
            "tests_folder/manipulated_from_pdf.pdf",
            "tests_folder/manipulated_from_image.jpg",
            "tests_folder/manipulated_from_image.pdf",
            "tests_folder/encoding_koi8.txt"
        ]
        
        for file in files:
            with self.assertRaises((ManipulatedFileError, MimeTypeNotDetectable)):
                detector.detect_true_type(file)
        

if __name__ == '__main__':
    unittest.main()