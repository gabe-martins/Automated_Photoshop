import win32com.client
import os 
#from pathvalidate import sanitize_filename

class AutomatePh:
  app = None
  psd_file = None

  def __init__(self):
    self.app = win32com.client.Dispatch("Photoshop.Application")
    self.app.Visible = False 
  
  def closePhotoshop(self):
    self.app.Quit()

  def openPSD(self, filename):
    if os.path.isfile(filename) == False:
      self.closePhotoshop()
      return False   

    self.app.Open(filename)
    self.psd_file = self.app.Application.ActiveDocument
    
    return True
  
  def closePSD(self):
    if self.psd_file is None:
      raise Exception(FileExistsError)

    self.app.Application.ActiveDocument.Close(2)
  
  def updateLayer(self, Layer_name, text):
    if self.psd_file is None:
      raise Exception(FileExistsError)

    layer = self.psd_file.ArtLayers[Layer_name]
    layer_text = layer.TextItem
    layer_text.contents = text
    
    return True

  def exportJPEG(self, filename, folder='', quality=10):
    if self.psd_file is None:
      raise Exception(FileExistsError)

    full_path = os.path.join(folder, filename)
    options = win32com.client.Dispatch("Photoshop.ExportOptionsSaveForWeb")
    options.Format = 6
    options.Quality = quality
    self.psd_file.Export(ExportIn=full_path, ExportAs=2, Options=options)

    return os.path.isfile(full_path)
