import os

font_path = os.path.join(os.path.dirname(__file__), "fonts", "DejaVuSans.ttf")
print(f"Font path: {font_path}")
print(f"Font file exists: {os.path.exists(font_path)}")
