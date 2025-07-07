try:

    file1=open('sample.txt','r')
    print("Reading the file content:")
    reading_file=file1.read()
    print("Line1:",reading_file)
    file1.close()

    file1=open('sample.txt','w')
    writing_file=file1.write('It contains multiple lines\n')
    file1.close()

    file1=open('sample.txt','r')
    reading_file=file1.read()
    print("Line2:",reading_file)
    file1.close()
except FileNotFoundError:
      print("Error:The file 'sample.txt' was not found ")

