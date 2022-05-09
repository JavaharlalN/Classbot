class Game:
	def __init__(self, a=False):
		self.active = a

	def reply(self, v):
		try:
			return str(float(v) + 1)
		except Exception:
			return "Вы проиграли"

	def stop(self):
		self.active = False

	def start(self):
		self.active = True


game = Game()
