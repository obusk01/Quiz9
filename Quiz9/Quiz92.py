fout=open("myfile.txt","w")

line1="Once upon a time...\n"
line2="There was a boy...\n"
line3="The boy liked sharks...\n"
line4="And he liked fish...\n"
line5="The End...\n"

fout.write(line1)
fout.write(line2)
fout.write(line3)
fout.write(line4)
fout.write(line5)

fout.close()

fout1=open("myfile.txt","r")
for line in fout1:
    print(line)
