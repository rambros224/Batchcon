import os
import sys
from PIL import Image

def convert_to_ico(folder):
    if not os.path.isdir(folder):
        print(f"error: folder '{folder}' does not exist")
        return
    
    for filename in os.listdir(folder):
        filepath=os.path.join(folder, filename)
        
        if filename.lower().endswith((".png",".jpg",".jpeg",".bmp",".gif")):
            try:
                img=Image.open(filepath)
                ico_path=os.path.join(folder,os.path.splitext(filename)[0]+".ico")
                img.save(ico_path,format="ICO")
                print(f"Convereted: {filename} -> {ico_path}")
            except Exception as e:
                print(f"error converting {filename}: {e}")
                
if __name__=="__main__":
    if len(sys.argv) !=2:
        print("usage: batchcon <folder_name>")
    else:
        convert_to_ico(sys.argv[1])