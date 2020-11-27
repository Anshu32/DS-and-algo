def anagram(s1,s2):
	record = {}
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()

	if len(s1)!=len(s2):
		return False

	for i in s1:
		if i in record:
			record[i] += 1
		else:
			record[i] = 1

	for j in s2:
		if j in record:
			record[i] -= 1
		else:
			record[j] = 1

	if len(record.values()) == 0:
		return False

	return True

s1,s2  = input().split(',')
print (anagram(s1,s2))
