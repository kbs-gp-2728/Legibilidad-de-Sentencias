import tempfile
import unittest
from pathlib import Path
import pymupdf
from lectura import leer_archivo


class PruebasLectura(unittest.TestCase):
    def test_txt(self):
        with tempfile.TemporaryDirectory() as carpeta:
            p = Path(carpeta) / "ejemplo.txt"
            p.write_text("Texto de prueba.\n Segunda línea.", encoding="utf8")
            self.assertEqual(leer_archivo(p), "Texto de prueba. Segunda línea.")

    def test_pdf_con_texto(self):
        with tempfile.TemporaryDirectory() as carpeta:
            p = Path(carpeta) / "ejemplo.pdf"
            pdf = pymupdf.open()
            pagina = pdf.new_page()
            pagina.insert_text((72, 72), "Texto de prueba")
            pdf.save(p)
            pdf.close()
            self.assertIn("Texto de prueba", leer_archivo(p))

    def test_pdf_sin_texto(self):
        with tempfile.TemporaryDirectory() as carpeta:
            p = Path(carpeta) / "vacio.pdf"
            pdf = pymupdf.open()
            pdf.new_page()
            pdf.save(p)
            pdf.close()
            with self.assertRaisesRegex(ValueError, "OCR"):
                leer_archivo(p)

    def test_extension_no_compatible(self):
        with tempfile.TemporaryDirectory() as carpeta:
            p = Path(carpeta) / "ejemplo.docx"
            p.write_text("Prueba", encoding="utf8")
            with self.assertRaisesRegex(ValueError, "Formato no compatible"):
                leer_archivo(p)


if __name__ == "__main__":
    unittest.main()
