#!/usr/bin/env python
# Graph dictionary
map_a = {
	# Each key represents a node with its associated children in a list
	1:[2,3],
	2:[4,5],
	3:[6,7],
	# Note that an child-less node needs a list to avoid an OOB error
	4:[],
	5:[8],
	6:[],
	7:[9,10],
	8:[],
	9:[],
	10:[],
}


# Second map

map_b = {
	7:[3,1,5],
	3:[4,9,10],
	1:[10, 1, 7],
	5:[13, 27, 7],
	4:[27, 3],
	9:[3],
	10:[1, 3],
	13:[1, 5],
	27:[5,4]
}

def bfs(goal, start):
	# Create a queue list populated by the start var
	queue = [start]
	# Create a discarded / not relevant list
	discarded = []

	# Initiate the queue loop
	while queue:
		print "Discarded: " + str(discarded) + " Queue: " + str(queue)
		# Set current as first element in list 
		current = queue.pop(0)

		if current == goal:
			# No need to carry on with function if goal is found
			return "Found."
		else:
			# Check each child from current node
			for child in map_a[current]:
				# Check if child has already been checked into discarded
				if child not in discarded:
					# Add child into right side of queue
					queue.append(child)
			# Discard current
			discarded.append(current)

	return "Not found."

print bfs(10, 1)