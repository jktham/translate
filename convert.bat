@echo off
echo starting conversion

for /l %%x in (1, 1, 11) do echo processing %%x & ("C:/Program Files/Tesseract-OCR/tesseract" C:/Users/Jonas/translate/%%x.jpg stdout 1>> C:/Users/Jonas/translate/output1.txt -l ita)

echo done
pause