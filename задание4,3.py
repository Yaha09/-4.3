
count_lines = {}

for line in open(r"q4_urls.txt",'rb'):
    clear_line = line.rstrip()
    if clear_line not in count_lines:
        count_lines[clear_line.rstrip()] = 0
    count_lines[clear_line.rstrip()] += 1



out1 = open(r"выход1.txt",'w')
num = 0

for line in sorted(count_lines.items(),reverse=True,key=lambda x: (x[1],x[0])):
    out1.write(f'№{num} кол-во.{line[1]} :   {line[0]}\n')  
    num += 1
out1.close()

print('ГОТОВО')


