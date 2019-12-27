person3={'Name':'Ford Prefect',
		 'Gender':'Male',
		 'Occupation':'Researcher',
		 'Home Planet':'Betelgeuse Seven'}
print(person3)
person3['Age']=33 #Add key value pair Just like .Add(key,value)
found={} #Dict need init before used
found['a']=6
found['e']=1
found['i']=5
found['o']=3
found['u']=4
print(found)
for k in found: # k not the <key,value> in Dict but only the key
	print(k,found[k])
for k,v in found.items(): #itmes() is the <key,value> list 
	print(k,v)
print(found)
print(found.items())

if 'z' not in found: # init 2
	found['z']=1

found.setdefault('z',1) #init 1

sortTest={1,3,5,2,4}
print(sorted(sortTest)) #sorted is the inner function for sort from the small to big


setTest1={'1','1','2','2','3','4','5'} #set init
setTest2=set('1122345') #set easy init 
print(setTest1)
print(setTest2)
