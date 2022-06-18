import os
import re


##mettre le liens du css a la place de l'inner-css

##remplacer le premier HR par <div class="main">

##remplacer le deuxieme HR par </div>

##remplacer 
regex = """<A HREF="RM-SRCH.html">Search</A>"""


directory = os.listdir("""C:\\Stage\\Documentation\\Ada_reference_manual_1995""")

for file in directory:
	actualFile = open(""".\\Ada_reference_manual_1995\\"""+file, "rt")
	data = actualFile.read() ;
	data = data.replace(regex,"""<A HREF="../RM-SRCH.html">Search</A>&nbsp;""")
	
	actualFile.close()
	newFile = open(""".\\Ada_reference_manual_1995\\"""+file, "wt")
	newFile.write(data)
	newFile.close()

print("Text successfully replaced")