class Node:
	def __init__(self, point):
		self.point = point
		self.left = None
		self.right = None

# Inserts new node and returns modified tree, depth is needed for axis
def _insert(root, point, depth):
	if not root:
		return Node(point)

	# Calculate current dimension (cd)
	cd = depth % k

	# Compare the new point with root on current dimension
	if point[cd] < root.point[cd]:
		root.left = _insert(root.left, point, depth + 1)
	else:
		root.right = _insert(root.right, point, depth + 1)

	return root

# Function to insert a new point with given point in KD Tree and return new root
def insert(root, point):
	return _insert(root, point, 0)

# A utility method to determine if two Points are same in K Dimensional space
def are_points_same(point1, point2):
	for i in range(k):
		if point1[i] != point2[i]:
			return False
	return True

# Searches a Point in the K D tree, depth is used to determine current axis
def _search(root, point, depth):
	if not root:
		return False
	if are_points_same(root.point, point):
		return True

	cd = depth % k

	if point[cd] < root.point[cd]:
		return _search(root.left, point, depth + 1)

	return _search(root.right, point, depth + 1)

def search(root, point):
	return _search(root, point, 0)

def distance(point1, point2):
    return sum([(point1[i] - point2[i]) ** 2 for i in range(k)])

def _find_nearest(self, root, point, depth=0, best=None):
		if not root:
			return best

		cur_dim = depth % self.k

		cur_node_distance = self.distance(root.point, point)
		if best is None or self.distance(best.point, point) > cur_node_distance:
			best = root
		
		if point[cur_dim] < root.point[cur_dim]:
			best = self._find_nearest(root.left, point, depth+1, best)
			if root.right and self.distance(best.point, point) > (point[cur_dim] - root.point[cur_dim])**2:
				best = self._find_nearest(root.right, point, depth+1, best)
		else:
			best = self._find_nearest(root.right, point, depth+1, best)
			if root.left and self.distance(best.point, point) > (point[cur_dim] - root.point[cur_dim])**2:
				best = self._find_nearest(root.left, point, depth+1, best)

		return best

	def find_nearest(self, point):
		return self._find_nearest(self.root, point)

	def _find_inside_rect(self, root, rect, depth=0, inside=None):
		if inside is None:
			inside = []

		if not root:
			return inside

		cur_dim = depth % self.k

		if rect[0][cur_dim] <= root.point[cur_dim] <= rect[1][cur_dim]:
			if all([rect[0][i] <= root.point[i] <= rect[1][i] for i in range(self.k)]):
				inside.append(root.point)
		
		if rect[0][cur_dim] <= root.point[cur_dim]:
			self._find_inside_rect(root.left, rect, depth+1, inside)

		if rect[1][cur_dim] >= root.point[cur_dim]:
			self._find_inside_rect(root.right, rect, depth+1, inside)

		return inside

def find_inside_rect(self, rect):
		return self._find_inside_rect(self.root, rect)

def _find_inside_cir(self, root, center, radius, depth=0, inside=None):
		if inside is None:
			inside = []

		if not root:
			return inside

		cur_dim = depth % self.k
		if center[cur_dim] - radius <= root.point[cur_dim] <= center[cur_dim] + radius:
			if all([center[i] - radius <= root.point[i] <= center[i] + radius for i in range(self.k)]):
				if self.distance(root.point, center) <= radius**2:
					inside.append(root.point)

		if center[cur_dim] - radius < root.point[cur_dim]:
			self._find_inside_cir(root.left, center, radius, depth+1, inside)

		if center[cur_dim] + radius > root.point[cur_dim]:
			self._find_inside_cir(root.right, center, radius, depth+1, inside)

		return inside

	def find_inside_cir(self, center, radius):
		return self._find_inside_cir(self.root, center, radius)
