class Stack:
     def init(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def dec2bin(decimal_input):
	binary = []
	decimal = decimal_input		
	while decimal > 0:
		binary.append(str(decimal % 2))
		decimal = int(decimal / 2)
	binary.reverse()
	return ''.join(binary)

print(' ***Decimal to Binary use Stack***')
decimal_input = int(input("Enter decimal number : "))
print("Binary number : ", end="")
print(dec2bin(decimal_input))