import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
def on_drop(event):
        # event.data contains the dropped file path(s)
        # For multiple files, it's a string with paths enclosed in braces and separated by spaces
        file_paths = event.data.strip().split('} {')
        cleaned_paths = [path.strip('{}') for path in file_paths]
        print(cleaned_paths[0])
        filename =  os.path.splitext(os.path.basename(cleaned_paths[0]))[0]
        filename += "_formatted.txt"
        dirpath = os.path.dirname(cleaned_paths[0])
        print(filename)
        formattedText = ""
        with open(cleaned_paths[0]) as file:
                formattedText = formatAA(file.read())
                file.close()
        with open(dirpath+"/"+filename,"w", encoding='utf-8') as newFile:
                newFile.write(formattedText)
                newFile.close()
        



def formatAA(text):
  print(text)
  escaped_text = text.replace('`', '\\`')
  return f"`{escaped_text}`"

window = TkinterDnD.Tk()
window.title("AA-formatter")
window.geometry("300x200")
window.drop_target_register(DND_FILES)
window.dnd_bind('<<Drop>>',on_drop)
label = tk.Label(window, text="Drag and drop AATextDatafiles here",)
label.pack(fill="both", expand=True, padx=20, pady=20)


window.mainloop()