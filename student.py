class Fruit(object):
	"""docstring for Fruit"""
	def __init__(self, name):
		self.name = name

	def details(self):
		print("Fruit name is ", self.name)

	@classmethod
	def info(self):
		print("THis is fruit class")
		

if __name__ == '__main__':
	f = Fruit("Mango")
	f.details()
	Fruit.info()