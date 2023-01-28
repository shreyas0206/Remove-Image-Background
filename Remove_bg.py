'''
Remove image background using python
'''
from rembg import remove
import easygui
from PIL import Image
input_path = easygui.fileopenbox(title='Select Image ')
output_path = easygui.filesavebox(title='Save File To ')
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
