import os
import re


##mettre le liens du css a la place de l'inner-css

##remplacer le premier HR par <div class="main">

##remplacer le deuxieme HR par </div>

##remplacer 
regex = """</HEAD>"""


directory = os.listdir(""".\\Ada_reference_manual_2012""")

for file in directory:
	actualFile = open(""".\\Ada_reference_manual_2012\\"""+file, "rt")
	data = actualFile.read() ;
	data = data.replace(regex,"""<link rel="icon" href="../logo.svg"></HEAD>""")
	
	actualFile.close()
	newFile = open(""".\\Ada_reference_manual_2012\\"""+file, "wt")
	newFile.write(data)
	newFile.close()

print("Text successfully replaced")