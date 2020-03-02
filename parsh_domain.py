read_file = open("domains.txt",'rt')
write_file = open("result.txt",'at')
for line in read_file:
    print(line.replace("\t","\n"))
    write_file.write(line.replace("\t","\n"))
read_file.close()
write_file.close()