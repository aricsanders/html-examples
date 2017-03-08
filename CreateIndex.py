# Creates index for html examples
import os
import re

files=os.listdir(os.getcwd())
index_template="<html><head></head><body><ol>{0}</ol></body>"
li_template="<li><a href='{0}'>{0}</a></li>"
li_string=""
for file in files:
    extension=file.split(".")[-1]
    if re.search("htm",extension,re.IGNORECASE):
        li_string=li_string+li_template.format(file)
out_string=index_template.format(li_string)
out_file=open("index.html",'w')
out_file.write(out_string)
out_file.close()
