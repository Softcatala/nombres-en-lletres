import io
import re

file_input="ca.sor"
file_output="ca-numbertext.js"

with io.open(file_input, 'r', encoding='utf-8') as f:
 text=f.read()

fo = io.open(file_output, 'w', encoding='utf-8')

fo.write(u"var rules_ca = `\n")

for line in text:
 linia = line.replace('\\', '\\\\')
 fo.write(linia)

fo.write(u"`")

f.close()
fo.close() 
