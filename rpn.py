#!/usr/bin/env python3

def calculate(arg):
	stack = list()
	for token in arg.split():
		#print(token)
		if token == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		else:
			stack.append(int(token))

		print(stack)
	return stack.pop()

def main():
	while True:
		result=calculate(input("rpn calc> "))
		print(result)


if __name__ == '__main__':
	main()
