f=open("AdventOfCode\input-day1.txt");
x=f.read()
first,second = [],[]

#Answer for 1st part
sum = 0
l = list(map(lambda x: x.split('   '), x.split('\n')))
for i in l:
    try:
        first.append(i[0])
        second.append(i[1])
    except:
        pass

first.sort()
second.sort()

for i in range(len(first)):
    sum += abs(int(first[i])-int(second[i]))
print(sum)


#Answer of 2nd part
product = 0
for i in first:
    sum += int(i)*int(second.count(i))
print(product)