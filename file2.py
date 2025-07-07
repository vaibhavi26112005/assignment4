file2=open('output.txt','w')
n=input("Enter text to write to the file:")
writing_file=file2.write(n)
file2.close()

file2=open('output.txt','r')
reading_file=file2.read()
print("Data successfully written to output.txt.\n\n")
file2.close()

file2=open('output.txt','a')
d=input("Enter additional text to append:")
appended_file=file2.write( '\n'+d)
file2.close()

file2=open('output.txt','r')
reading_file=file2.read()
print("Data successfully appended.\n\n")
file2.close()

file2=open('output.txt','r')
print("Final content of output.txt:")
reading_file=file2.read()
print(reading_file)
file2.close()







