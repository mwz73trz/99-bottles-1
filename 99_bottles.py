def bottle_song(num):
	total = num
	while num > 2:
		print(f"{num} bottles of beer on the wall, {num} bottles of beer.")
		print("Take one down and pass it around,")
		num -= 1
		print(f"{num} bottles of beer on the wall.")
	while num == 2:
		print(f"{num} bottles of beer on the wall, {num} bottles of beer.")
		print("Take one down and pass it around,")
		num -= 1
		print(f"{num} bottle of beer on the wall.")
	while num == 1:
		print(f"{num} bottle of beer on the wall, {num} bottle of beer.")
		print("Take one down and pass it around,")
		num -= 1
		print("No more bottles of beer on the wall.") 
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print(f"Go to the store and buy some more, {total} bottles of beer on the wall.")


bottle_song(5)
