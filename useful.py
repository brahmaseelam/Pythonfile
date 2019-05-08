import re
f=with open('C:\\Users\\Brahmareddy\\Desktop\\invoice automation.txt')
	for i in f:
		match=re.match(r'([^a-zA-Z0-9]+.*) ',i)
			if match!=None:
				print(match.group())
			else:
				print('not matched')



# how to sort a list without using built-in function

