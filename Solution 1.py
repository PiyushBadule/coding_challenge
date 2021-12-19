# Question:- Reverse each words in sentence without using library function. LIKE “SPLIT”
#  e.g  input: "I Love my India"  output "India my Love I"
a = "I Love my India"
x = ""
for i in range(len(a)-1,-1,-1):
    if(a[i] == " "):
        for n in range(len(x)-1, -1, -1):
            print(x[n], end='')
        print(end=' ')
        x = ""
    else:
        x = x+a[i]
for n in range(len(x)-1, -1, -1):
    print(x[n], end='')
