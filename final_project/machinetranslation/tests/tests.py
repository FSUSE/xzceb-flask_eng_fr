import unittest
from translator import french_to_english, english_to_french

class Testtranslator(unittest.TestCase):
    def test_english_to_french(self):
        #Test for null input
        self.assertIsNone(english_to_french(None))

        #Test for valid input
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


    def test_french_to_englsich(self):
        # Test for null inout 
        self.assertIsNone(french_to_english(None))

        # Test for valid input
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_helloBonjourTranslation(self):
        # Test english to french 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

        # Test french to english
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_bonjourHelloTranslation(self):
        # Test french to english translation
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

        # Test english to french translation
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()