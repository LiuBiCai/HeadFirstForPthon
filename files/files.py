todos=open('todos.txt','a') #append r read w write x create
print("test",file=todos)
todos.close()
tasks=open('todos.txt')
for chore in tasks:
	print(chore)
tasks.close()

with open('todos.txt') as tasks: # just like using 
	for chore in tasks:
		print(chore)



