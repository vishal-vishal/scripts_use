domain_open = open('result.txt','rt')
domain_write = open('new_result.txt','at')

for line in domain_open:
    if ".com" in line:
        print(line)
        domain_write.write(line)

domain_open.close()
domain_write.close()