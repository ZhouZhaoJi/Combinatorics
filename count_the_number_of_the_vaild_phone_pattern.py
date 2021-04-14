from itertools import permutations

invalids = {
"13":"2","31":"2",
"46":"5","64":"5",
"79":"8","97":"8",
"17":"4","71":"4",
"28":"5","82":"5",
"39":"6","93":"6",
"19":"5","91":"5",
"37":"5","73":"5"
}

total = 0

for i in range(4, 10):
	count = 0
	for perm in permutations([str(j) for j in range(1,10)], i):
		perm_str = "".join(perm)
		for k,v in invalids.items():
			index = perm_str.find(k)
			if index == -1 or v in perm_str[0:index]:
				continue
			else:
				break
		else:
			count = count + 1
	print(f"When i = {i}, the number of the vaild pattern is {count}.")
	total = total + count
print(f"when i is in 4 up to 9, the number of the vaild pattern is {total}.")