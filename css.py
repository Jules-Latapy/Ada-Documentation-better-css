import os
import re

def StringReplacementInFolder(motif,replacement,regex=False,dirList=["./Ada_reference_manual_2012","./Ada_reference_manual_1995"]):

	for di in dirList:
		directory = os.listdir(di)

		for file in directory:

			if file.endswith('.html'):
				
				actualFile = open(di +"\\"+file, "rt")
				data = actualFile.read() ;

				if regex:
					data = re.sub(motif,replacement,data,count=1,flags=re.DOTALL)
				else:
					data = data.replace(motif,replacement,1)
				
				actualFile.close()
				newFile = open(di + "\\"+file, "wt")
				newFile.write(data)
				newFile.close()


"""mettre le liens du css a la place de l'inner-css                 """     
#StringReplacementInFolder(r"<STYLE.*</STYLE>", """<link rel="stylesheet" href="../styles.css">\n\t<link rel="icon" href="../logo.svg">""",True)

"""remplacer le premier HR par <div class="main">                   """ 
#StringReplacementInFolder("<HR>",'<div class="main">')

"""remplacer le deuxieme HR par </div>                              """     
#StringReplacementInFolder("<HR>",'</div>')

"""remplacer la fin de l'entete par la l'icon+ la fin de l'entete   """     
#StringReplacementInFolder("""</div>
#<div class="main">""","""<img SRC="../logo.svg" class="adaLogo">
#</div>
#<div class="main">""")

"""remplacer la div par la class navig qui indique les liens pour naviguer"""   
#StringReplacementInFolder('<div style="margin-top: 0.0em; margin-bottom: 0.6em">','<div class="navig">',dirList=["./Ada_reference_manual_2012"])
#StringReplacementInFolder("""<BODY TEXT="#000000" BGCOLOR="#FFFFF0" LINK="#0000FF" VLINK="#800080" ALINK="#FF0000">
#<P>""","""<BODY TEXT="#000000" BGCOLOR="#FFFFF0" LINK="#0000FF" VLINK="#800080" ALINK="#FF0000">
#<div class="navig">""")

"""remplace les image moche
StringReplacementInFolder('<IMG SRC="cont.gif" ALT="Contents" BORDER=0>','Contents')
StringReplacementInFolder('<IMG SRC="index.gif" ALT="Index" BORDER=0>','Index')
StringReplacementInFolder('<IMG SRC="lib.gif" ALT="References" BORDER=0>','References')
StringReplacementInFolder('<IMG SRC="find.gif" ALT="Search" BORDER=0>','Search')
StringReplacementInFolder('<IMG SRC="next.gif" ALT="Next" BORDER=0>','Next')
StringReplacementInFolder('<IMG SRC="prev.gif" ALT="Previous" BORDER=0>','Previous')
StringReplacementInFolder('<IMG SRC="AE_logo.gif" height=100 width=113 align=right ALT="Ada-Europe">',"")
"""

#StringReplacementInFolder("""</P>
#<div class="main">""","""<img SRC="../logo.svg" class="adaLogo">
#</div>
#<div class="main">""")



#StringReplacementInFolder("""<P><A HREF="AA-TOC.html">Contents""","""<div class="navig"><P><A HREF="AA-TOC.html">Contents""")

#StringReplacementInFolder("""</P>
#</BODY>
#</HTML>""","""</div>
#</BODY>
#</HTML>""")


"""Remplacement de lien de recherche"""
#StringReplacementInFolder("""<A HREF="AA-SRCH.html">""","""<A HREF="../RM-SRCH.html">""")

"""
	<STYLE type="text/css">
    DIV.paranum {position: absolute; font-family: Arial, Helvetica, sans-serif; left: 0.5em; top: auto}
    TT {font-family: "Courier New", monospace}
    DT {display: compact}
    DIV.Normal {font-family: "Times New Roman", Times, serif; margin-bottom: 0.6em}
    DIV.Wide {font-family: "Times New Roman", Times, serif; margin-top: 0.6em; margin-bottom: 0.6em}
    DIV.Annotations {font-family: "Times New Roman", Times, serif; margin-left: 4.0em; margin-bottom: 0.6em}
    DIV.WideAnnotations {font-family: "Times New Roman", Times, serif; margin-left: 4.0em; margin-top: 0.6em; margin-bottom: 0.6em}
    DIV.Index {font-family: "Times New Roman", Times, serif}
    DIV.SyntaxSummary {font-family: "Times New Roman", Times, serif; margin-left: 2.0em; margin-bottom: 0.4em}
    DIV.Notes {font-family: "Times New Roman", Times, serif; margin-left: 2.0em; margin-bottom: 0.6em}
    DIV.NotesHeader {font-family: "Times New Roman", Times, serif; margin-left: 2.0em}
    DIV.SyntaxIndented {font-family: "Times New Roman", Times, serif; margin-left: 2.0em; margin-bottom: 0.4em}
    DIV.Indented {font-family: "Times New Roman", Times, serif; margin-left: 6.0em; margin-bottom: 0.6em}
    DIV.CodeIndented {font-family: "Times New Roman", Times, serif; margin-left: 4.0em; margin-bottom: 0.6em}
    DIV.SmallIndented {font-family: "Times New Roman", Times, serif; margin-left:  10.0em; margin-bottom: 0.6em}
    DIV.SmallCodeIndented {font-family: "Times New Roman", Times, serif; margin-left: 8.0em; margin-bottom: 0.6em}
    DIV.Examples {font-family: "Courier New", monospace; margin-left: 2.0em; margin-bottom: 0.6em}
    DIV.SmallExamples {font-family: "Courier New", monospace; font-size: 80%; margin-left: 7.5em; margin-bottom: 0.6em}
    DIV.IndentedExamples {font-family: "Courier New", monospace; margin-left: 8.0em; margin-bottom: 0.6em}
    DIV.SmallIndentedExamples {font-family: "Courier New", monospace; font-size: 80%; margin-left:  15.0em; margin-bottom: 0.6em}
    UL.Bulleted {font-family: "Times New Roman", Times, serif; margin-left: 2.0em; margin-right: 2.0em; margin-top: 0em; margin-bottom: 0.5em}
    UL.SmallBulleted {font-family: "Times New Roman", Times, serif; margin-left: 6.0em; margin-right: 6.0em; margin-top: 0em; margin-bottom: 0.5em}
    UL.NestedBulleted {font-family: "Times New Roman", Times, serif; margin-left: 4.0em; margin-right: 4.0em; margin-top: 0em; margin-bottom: 0.5em}
    UL.SmallNestedBulleted {font-family: "Times New Roman", Times, serif; margin-left: 8.0em; margin-right: 8.0em; margin-top: 0em; margin-bottom: 0.5em}
    UL.IndentedBulleted {font-family: "Times New Roman", Times, serif; margin-left: 8.0em; margin-right: 8.0em; margin-top: 0em; margin-bottom: 0.5em}
    UL.CodeIndentedBulleted {font-family: "Times New Roman", Times, serif; margin-left: 6.0em; margin-right: 6.0em; margin-top: 0em; margin-bottom: 0.5em}
    UL.CodeIndentedNestedBulleted {font-family: "Times New Roman", Times, serif; margin-left: 8.0em; margin-right: 8.0em; margin-top: 0em; margin-bottom: 0.5em}
    UL.SyntaxIndentedBulleted {font-family: "Times New Roman", Times, serif; margin-left: 4.0em; margin-right: 4.0em; margin-top: 0em; margin-bottom: 0.5em}
    UL.NotesBulleted {font-family: "Times New Roman", Times, serif; margin-left: 4.0em; margin-right: 4.0em; margin-top: 0em; margin-bottom: 0.5em}
    UL.NotesNestedBulleted {font-family: "Times New Roman", Times, serif; margin-left: 6.0em; margin-right: 6.0em; margin-top: 0em; margin-bottom: 0.5em}
    DL.Hanging {font-family: "Times New Roman", Times, serif; margin-top: 0em; margin-bottom: 0.6em}
    DD.Hanging {margin-left: 6.0em}
    DL.IndentedHanging {font-family: "Times New Roman", Times, serif; margin-left: 4.0em; margin-top: 0em; margin-bottom: 0.6em}
    DD.IndentedHanging {margin-left: 2.0em}
    DL.HangingInBulleted {font-family: "Times New Roman", Times, serif; margin-left: 2.0em; margin-right: 2.0em; margin-top: 0em; margin-bottom: 0.5em}
    DD.HangingInBulleted {margin-left: 4.0em}
    DL.SmallHanging {font-family: "Times New Roman", Times, serif; margin-left: 4.0em; margin-top: 0em; margin-bottom: 0.6em}
    DD.SmallHanging {margin-left: 7.5em}
    DL.SmallIndentedHanging {font-family: "Times New Roman", Times, serif; margin-left: 8.0em; margin-top: 0em; margin-bottom: 0.6em}
    DD.SmallIndentedHanging {margin-left: 2.0em}
    DL.SmallHangingInBulleted {font-family: "Times New Roman", Times, serif; margin-left: 6.0em; margin-right: 6.0em; margin-top: 0em; margin-bottom: 0.5em}
    DD.SmallHangingInBulleted {margin-left: 5.0em}
    DL.Enumerated {font-family: "Times New Roman", Times, serif; margin-right: 0.0em; margin-top: 0em; margin-bottom: 0.5em}
    DD.Enumerated {margin-left: 2.0em}
    DL.SmallEnumerated {font-family: "Times New Roman", Times, serif; margin-left: 4.0em; margin-right: 4.0em; margin-top: 0em; margin-bottom: 0.5em}
    DD.SmallEnumerated {margin-left: 2.5em}
    DL.NestedEnumerated {font-family: "Times New Roman", Times, serif; margin-left: 2.0em; margin-right: 2.0em; margin-top: 0em; margin-bottom: 0.5em}
    DL.SmallNestedEnumerated {font-family: "Times New Roman", Times, serif; margin-left: 6.0em; margin-right: 6.0em; margin-top: 0em; margin-bottom: 0.5em}
    </STYLE>,
"""