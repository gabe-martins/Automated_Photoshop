import sys, os
import unittest

sys.path.insert(0, './src')

from automate_ph import Automate_ph

class TestPh(unittest.TestCase):

    def setUp(self):
      
        self.psd_origin = os.path.abspath('./tests/resources/test.psd')
        self.jpeg_path = os.path.abspath('./tests/resources/tmp')
        self.jpeg_name = "test-01.jpg"
        self.jpeg_full_path = os.path.join(self.jpeg_path, self.jpeg_name)

        if not os.path.exists(self.jpeg_path):
          os.mkdir(self.jpeg_path)

        self.app = Automate_ph()

    def tearDown(self):
      self.app.closePhotoshop()

      # if os.path.exists(self.jpeg_full_path):
      #   os.remove(self.jpeg_full_path)

      if os.path.exists(self.jpeg_path):
        os.rmdir(self.jpeg_path)

    def test_openPSD(self):
      opened = self.app.openPSD(self.psd_origin)
      if opened:
        self.app.closePSD()
      self.assertTrue(opened)
    
    def test_updateLayer(self):
      updated1 = False
      updated2 = False

      opened = self.app.openPSD(self.psd_origin)
      if opened:
          updated1 = self.app.updateLayer("Palavra", "Hello")
          updated2 = self.app.updateLayer("Frase", "Hello World!")
          self.app.closePSD()

      self.assertTrue(updated1)
      self.assertTrue(updated2)
    
      def test_exportJPEG(self):
        exported = False

        opened = self.app.openPSD(self.psd_origin)
        if opened:
            updated1 = self.app.updateLayer("Palavra", "Hello")
            updated2 = self.app.updateLayer("Frase", "Hello World!")

            if updated1 & updated1:
              exported = self.app.exportJPEG

            self.app.closePSD()

        self.assertTrue(exported)

if __name__ == '__main__':
  unittest.main()
