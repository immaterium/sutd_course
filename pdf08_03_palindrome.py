def is_palindrome(integer):
	integer = str(integer)
	while len(integer) > 1:
		left_pos = 0
		right_pos = len(integer) - 1

		if not integer[left_pos] == integer[right_pos]:
			return False
		else:
			integer = integer[left_pos+1:right_pos]
			is_palindrome(integer)
	return True

print("Test case 1: 1")
ans=is_palindrome(1)
print(ans)

print("Test case 2: 22")
ans=is_palindrome(22)
print(ans)

print("Test case 3: 12321")
ans=is_palindrome(12321)
print(ans)

print("Test case 4: 441232144")
ans=is_palindrome(441232144)
print(ans)

print("Test case 5: 441231144")
ans=is_palindrome(441231144)
print(ans)

print("Test case 6: 144")
ans=is_palindrome(144)
print(ans)

print("Test case 7: 12")
ans=is_palindrome(12)
print(ans)
