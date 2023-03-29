print("Digite um número")
a=float(input())    
print("Qual operação você quer fazer?")  
c=input()


c=c.lower()

if c=="ao quadrado":
    print (a**2)
    quit() 

b=float(input())


if c=="*":
    print(a*b)
    
elif c=="/":
    print(a/b)

elif c=="-":
    print(a-b)

elif c=="+":
    print(a+b)


