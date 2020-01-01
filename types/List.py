from datetime import datetime
odds=[1,3,5,7,9,11,13,15,17,19]
right_this_minute=datetime.today().minute
if right_this_minute in odds:
	print ("This is odd")
else:
		print ("not")
print (odds[::2])
print (odds[-2:])


slice=odds[::2] #slice is a deep copy
slice0=odds
slice1=odds[::]
odds.remove(1)
print(slice)
odds[::2].pop()
print(slice)
print(slice0)
print(slice1)

phrase="Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)
for i in range(4):
	plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
print(plist)
plist.insert(2,plist.pop(3))
new_phrase=' '.join(plist)
print(plist)
print(new_phrase)
for char in plist[:4]:
	print('\t'*2,char)
for char in plist[4:]:
	print('\t'*4,char)

