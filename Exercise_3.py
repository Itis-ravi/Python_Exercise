x = int(input('Enter a number to begin\n'))
div_li = []

i = 1
while i<=x:
    if x%i==0:
        div_li.append(i)

    i+=1

print(div_li)
