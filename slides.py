import os
file = input("\nNotebook name: ")
os.system(f'..\..\appdata\roaming\python\python311\scripts\jupyter nbconvert notebooks\{file}.ipynb --to slides --SlidesExporter.reveal_scroll=True')
os.system(f"move notebooks\{file}.slides.html docs\{file}.slides.html")
os.system("git add .")
os.system('git commit -m "new slides"')
os.system("git push origin main")