import unittest

from Problème_1 import img2ascii, load

img = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

tests = [
    (img, None, None, '..........\n..######..\n.##....##.\n.#......#.\n.#......#.\n.#......#.\n.#......#.\n.##....##.\n..######..\n..........'),
    (img, 'O', ' ', '          \n  OOOOOO  \n OO    OO \n O      O \n O      O \n O      O \n O      O \n OO    OO \n  OOOOOO  \n          '),

]

class MyTests(unittest.TestCase):

    def test_1(self):
        for img, black, white, expected in tests:
            black = black or '#'
            white = white or '.'
            result = img2ascii(img, black, white)
            self.assertEqual(result, expected)

class TestLoadPBM(unittest.TestCase):
    
    def test_1(self):
        for filename, expected in tests:
            path = f''
            result = load_pbm()
            feedback = f"Le fichier filename={filename} est chargé correctement"
            self.assertEqual(result, expected, feedback)
if __name__ == '__main__':
    unittest.main()