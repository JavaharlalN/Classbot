class Game:
	def __init__(self, a=False):
		self.active = a

	def reply(self, v):
		if v.isdigit():
			return str(int(v) + 1)
		return "Вы проиграли"

	def stop(self):
		self.active = False

	def start(self):
		self.active = True


game = Game()
