import os
file = input("\nNotebook name: ")
os.system(f'jupyter nbconvert notebooks\{file}.ipynb --to slides --SlidesExporter.reveal_scroll=True')
os.system(f'decktape automatic notebooks\{file}.slides.html notebooks\{file}.slides.pdf')
os.system(f"move notebooks\{file}.slides.html docs\{file}.slides.html")
os.system(f"move notebooks\{file}.slides.pdf pdfs\{file}.slides.html")
os.system("git add .")
os.system('git commit -m "new slides"')
os.system("git push origin main")