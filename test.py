def on_alamhulk(hulk1,hulk2):
	if hulk1 == hulk2:
		print("ja")
	if hulk1 in hulk2:
		print("hulk1")
	if hulk2 in hulk1:
		print("hulk2")

def võrdle_hulki(hulk1,hulk2):
	pass


hulk1 = {3,5}
hulk2 = {3}

print(on_alamhulk(hulk1,hulk2))