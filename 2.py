str="helloWorld"
n=5
l=[str[i:i+n] for i in range(0, len(str), n)]
print(l)
