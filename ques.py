total_city = {'a','b','c','d','e','f','g','h','i','j'}
print(total_city)
s1 = {'a','b','c'}
s2 = {'d','e'}
s3 = {'f','g','h'}
s = s1.union(s2,s3)
print(s)
rem = total_city - s
print(rem,len(rem))