@echo off
echo starting conversion

for /l %%x in (0, 1, 1) do echo processing %%x & ("C:/Program Files/Tesseract-OCR/tesseract" C:/Users/Jonas/projects/translate/input/%%x.jpg stdout 1>> C:/Users/Jonas/projects/translate/output/result.txt -l ita --psm 6)

echo done
pause