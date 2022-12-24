import sys
print("* Python Interpreter\n# Type 'Info' to get info,'Exit' to exit.")
print(">",end=" ")
n=(sys.stdin.readline())
while n!="Exit\n":
	n=n+"#"
	for i in range(len(n)):
		if n[i]=="#":
			n=n[0:i]
			break
	for j in range(len(n)-1,-1,-1):
		if n[j]==" " or n[j]=="\n" or n[j]=="\t":
			n=n[0:j]
		else:
			break
	n=n+"\n"
	if n=="Info\n":
		print("# A simple python interpreter using EXEC.\n# (So it is not very safe)\n# Enter code behind '>'.\n")
		print(">",end=" ")
		n=(sys.stdin.readline())
	elif len(n)>1 and n[-2]==":":
		print("# Use a non-block to stop entering.")
		print(">",end=" ")
		m=(sys.stdin.readline())
		while m[0]=="\t" or (len(m)>3 and m[0:4]=="    "):
			n=n+m
			print(">",end=" ")
			m=(sys.stdin.readline())
		print("$",end=" ")
		exec(n)
		n=m
	else:
		print("$",end=" ")
		exec(n)
		print(">",end=" ")
		n=(sys.stdin.readline())
print("# Thanks for using!")
