import os
file = input("\nNotebook name: ")
os.system(f'decktape automatic docs\{file}.slides.html docs\pdfs\{file}.slides.pdf')
