import unittest
import os

class TestWebPage(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.exists("index.html"), "El archivo index.html no existe")

    def test_contains_hola_mundo(self):
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("<h1>Hola Mundo</h1>", content, "El contenido 'Hola Mundo' no está presente")

if __name__ == "__main__":
    unittest.main()
