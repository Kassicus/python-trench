import pygame

pygame.init()

class Game():
	def __init__(self):
		self.screen = pygame.display.set_mode([1000, 800])
		pygame.display.set_caption("Python Trenches")

		self.running = True
		
		self.events = pygame.event.get()

		self.clock = pygame.time.Clock()
		self.delta_time = 0
		self.framerate = 120

	def start(self):
		while self.running:
			self.event_loop()
			self.draw()
			self.update()

	def event_loop(self):
		self.events = pygame.event.get()

		for event in self.events:
			if event.type == pygame.QUIT:
				self.running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					self.running = False

	def draw(self):
		self.screen.fill((0, 0, 0))

	def update(self):
		pygame.display.update()
		self.delta_time = self.clock.tick(self.framerate) / 1000

if __name__ == '__main__':
	game = Game()
	game.start()
	pygame.quit()