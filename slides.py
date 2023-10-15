import os
file = input("\nNotebook name: ")
os.system(f'jupyter nbconvert notebooks\{file}.ipynb --to slides --SlidesExporter.reveal_scroll=True')
os.system(f"move notebooks\{file}.slides.html docs\{file}.slides.html")