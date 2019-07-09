import functools
def note(func):
	'note function'
	def wrapper():
		'wrapper function'
		print("note something")
		return func()
	return wrapper

@note
def test():
	'test function'
	print("I am test")

print(help(test))
