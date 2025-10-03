'''
with open('learning_python.txt') as file_object:
	contents = file_object.read()
	

count = 1
while count <= 3:
	print("\n")
	print(contents.rstrip() + "\n")
	count += 1
	
	
filename = ('learning_python.txt')
with open(filename) as file_object:	
	for line in file_object:
		print(line.rstrip() + "\n")
'''		
		
filename = 'learning_python.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
	
lp_string = ''
for line in lines:
	line.replace('Python', 'C')
	print(line)
	lp_string += line.strip()
	
#print(lp_string[:12] + "...")
print(lines)
lines
#print(len(lp_string))
