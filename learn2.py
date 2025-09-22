words = ["paolo", "piastra", "primo"]
for w in words:
	print(w, len(w))

# The for statement in Python differs a bit from what you may be used to in C or Pascal.
# Rather than always iterating over an arithmetic progression of numbers (like in Pascal),
# or giving the user the ability to define both the iteration step and halting condition (as C),
# Python’s for statement iterates over the items of any sequence (a list or a string),
# in the order that they appear in the sequence.
#IT MEANS FOR LOOPS EXECUTE A BLOCK OF CODE A FIXED NUMBER OF ITEMS
#YOU SET HOW MANY TIMES IT WILL EXECUTE for **w** (times) in **Words**

for counter in range(1,11):
	print(counter)

for counter in reversed(range(1,11)):
	print(counter)

print("Happy New Year")

for counter in range(1, 11, 3):
	print(counter)

for x in range(1,21):
	if x == 13:
		continue
	else:
		print(x)

for x in range(1,21):
	if x == 13:
		break
	else:
		print(x)
	