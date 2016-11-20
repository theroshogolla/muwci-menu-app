array=[]
def sum_array():
	while True:
		num=input("Enter an number: ")
		if num!='':
			array.append(int(num))
		else:
			break
	return sum(array)
	
sum_array()
