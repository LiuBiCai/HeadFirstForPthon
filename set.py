setTest1={'1','1','2','2','3','4','5'} #set init
setTest2=set('1122345') #set easy init 
print(setTest1)
print(setTest2)

vowels=set('aeiou')
world='hello'
u=vowels.union(set(world))
print(u)
d=vowels.difference(set(world))
print(d)
i=vowels.intersection(set(world))
print(i)
