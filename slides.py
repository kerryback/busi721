import os
file = input("\nNotebook name: ")
os.system(f'jupyter nbconvert notebooks\{file}.ipynb --to slides --SlidesExporter.reveal_scroll=True')
os.system(f"move notebooks\{file}.slides.html docs\{file}.slides.html")
os.system(f"git add .")
os.system('git commit -m "new slides"')
os.system(f"git push origin main")