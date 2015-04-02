"""
Pacman Astar

"""

from game import Agent, Directions

class MovePacman(Agent):
	""" Trying to get pacman to move
	state.data.food from game.Grid

	"""

	def getAction(self, state):
		"""
		Pacman moves east
		"""
		legal_actions = state.getLegalActions()
		# print legal_actions
		if "East" in legal_actions:
			print state.data.capsules
			print dir(state)
			return Directions.EAST
		else:
			print state.data.capsules
			return Directions.STOP
		# pacman_location = 

	

class path():
	"""
	For example layout, food is in [(18, 1), (1,9)]. Bottom left-hand corner = (1,1)
	"""

	def __init__(self, draw_screen, coordinates, dimensions):
		self.draw_screen = draw_screen
		self.coordinates = coordinates
		self.dimensions = dimensions
		self.color = (0,0,0)
		self.g_cost = None
		self.h_cost = None

	def f_cost(self):
		""" 
		Function to optimize Pacman Path. F = G + H
		G = cost of moving from starting position to another position
		H = Number of squares left
		"""
		COST_TO_MOVE = ''
		COST_TO_MOVE = self.g_cost
		# COST_TO_MOVE = self.h_cost
		# COST_TO_MOVE = self.f_cost
		line_width = 2
		#Want to draw a line that displays pacman path using Astar search
