"""
Pacman Astar

"""

from game import Agent, Directions
from numpy import ones
import copy

class SetUp(object):
	"""Setting up the grid

	Potentially use this class to initialze the position of Pacman and the 
	importnat capsules.
	"""
	def __init__(self):
		pass

class Astar2Pacman(Agent):
	""" Trying to get pacman to move
	state.data.food from game.Grid
	"""

	def __init__(self): 
		"""Insert doc string"""
		pass

	def Astar(self, state, start, goal):
		"""Astar function that runs the show"""
		self.open_list = [] #Set of nodes already evaluated
		self.closed_list = [] #Tentative nodes to be evaluated
		self.current_tile = []

		costs = {} #The size of the game board to store g, h and f cost values
		for x in range(1,19):
			for y in range(1,10):
				costs[(x, y)] = Tile((x,y))
		costs[self.coordinates].g_cost = 0
		costs[self.coordinates].h_cost = self.get_h_cost(start, goal)
		costs[self.coordinates].f_cost = costs[self.coordinates].g_cost + costs[self.coordinates].h_cost
		self.open_list.append(costs[self.coordinates])

		while len(self.open_list) > 0:
			tile = self.get_lowest_cost_open_coord(self.open_list)
			print tile.coordinates
			self.open_list.remove(tile)
			self.closed_list.append(tile)

			open_coords, relative_direction, tile_cost = self.get_open_adj_coords(state, tile.coordinates)
			# print open_coords, relative_direction, tile_cost
			for i, coord in enumerate(open_coords):
				if coord == goal:
					print coord
					costs[coord].g_cost = tile.g_cost + tile_cost[i]
					costs[coord].h_cost = self.get_h_cost(coord, goal)
					costs[coord].f_cost = costs[coord].g_cost + costs[coord].h_cost
					print costs[coord].g_cost
					print costs[coord].h_cost
					print costs[coord].f_cost
					self.open_list = []
					break

				if costs[coord] in self.closed_list:
					pass
				elif costs[coord] not in self.open_list:
					self.open_list.append(costs[coord])
					costs[coord].g_cost = tile.g_cost + tile_cost[i]
					costs[coord].h_cost = self.get_h_cost(coord, goal)
					costs[coord].f_cost = costs[coord].g_cost + costs[coord].h_cost
					costs[coord].parent = tile
				elif coord in self.open_list:
					if costs[coord].f_cost > costs[coord].g_cost + costs[coord].h_cost:
						costs[coord].f_cost = costs[coord].g_cost + costs[coord].h_cost
						costs[coord].parent = tile

	def getAction(self, state):
		"""
		Pacman moves east
		"""
		self.coordinates = state.getPacmanPosition()
		self.capsule1_coords = state.data.capsules[0] 
		self.capsule2_coords = state.data.capsules[1]

		self.Astar(state, self.coordinates, self.capsule1_coords)

		legal_actions = state.getLegalActions()
		if "East" in legal_actions:
			return Directions.EAST
		else:
			return Directions.STOP


	def get_h_cost(self, coord_a, coord_b):
		"""Returns the h score, the manhattan distance between coord_a and the cood_b"""
		return abs(coord_a[0] - coord_b[0]) + abs(coord_a[1] - coord_b[1])


	def get_open_adj_coords(self, state, coords):
		"""returns list of valid coords that are adj. to the pacman, open 
		(and are not in the closed list(?))"""
		adj_coords = []
		d = []
		configuration_copy = copy.deepcopy(state.getPacmanState().configuration)
		configuration_copy.pos = coords
		# print dir(state)s
		print state.__class__.__name__
		directions = state.getLegalActions_Tile(configuration_copy, state)
		directions.remove("Stop")
		if "West" in directions:
			W_coords = (coords[0]-1, coords[1])
			d.append("West")
			adj_coords.append(W_coords)
		if "East" in directions:
			E_coords = (coords[0]+1, coords[1])
			d.append("East")
			adj_coords.append(E_coords)
		if "North" in directions:
			N_coords = (coords[0], coords[1]+1)
			adj_coords.append(N_coords)
			d.append("North")
		if "South" in directions:
			S_coords = (coords[0], coords[1]-1)
			d.append("South")
			adj_coords.append(S_coords)
		costs = [1]*len(adj_coords)

		return adj_coords, d, costs

	
	def get_lowest_cost_open_coord(self, open_list):
		"""Return the tile with the lowest cost"""
		return sorted(open_list, key = lambda t: t.f_cost)[0]


	def reconstruct_path(open_list, current):
		total_path = [current]
		while current in open_list:
			print current
			total_path.append(current)
		return total_path


class Tile():
	"""
	For example layout, food is in [(18, 1), (1,9)]. Bottom left-hand corner = (1,1)
	"""
	def __init__(self, coordinates, parent = None, g_cost = None, h_cost = None, f_cost = None):
		self.coordinates = coordinates
		self.parent = parent
		self.g_cost = g_cost
		self.h_cost = h_cost
		self.f_cost = f_cost

	def __str__(self):
		return str(self.coordinates)

	def __repr__(self):
	    return str(self.coordinates)