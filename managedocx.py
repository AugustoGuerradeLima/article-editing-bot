import docx
import json

#open the arq .docx
doc = docx.Document('doc.docx')

#put first paragraph on title
title = doc.paragraphs[0].text

#create an object JSON with title, info and content
text = {
    "title":title,
    "info":"info",
    "content":"content"
}

                                                                        #text zone

#JSON for string
text = json.dumps(text,indent=4)

#Print the variable text on screen
print(text)
