""" 
This code takes an extended star with arm lengths 3, 2, 2 respectively and spreads a message starting from a central node. Message is passed to a random neighbor with a probability phi.

"""

import graph_tool.all as gt
import numpy as np

# Construct the extended star with a given arm lengths
g = gt.Graph(directed = False)
g.add_edge_list([(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (0, 6), (6, 7)])

# Create vertex properties to keep track of whether a vertex has a message or not
state_old = g.new_vertex_property('int')
state_new = g.new_vertex_property('int')

# Open a file to record the total amount of times needed
f = open('tot_times.dat', 'w')

# Loop over the realizations

for ind in range(5000):

    # Initialize the states: 0 and 1 represent the absense and the presence of the message 
    for v in g.vertices():
        state_old[v] = 0
        state_new[v] = 0
    
    # Put a message on a central node
    state_old[0] = 1
    state_new[0] = 1
    
    # Specify the probability of spread
    phi = 0.3
    
    # Start the spread
    tot_infected_nodes = 1
    t = 0
    
    while tot_infected_nodes < g.num_vertices():
        # Spread the message to the neighbours
        for v in g.vertices():
            if state_old[v] == 1:
                for nbr in v.out_neighbours():
                    if state_old[nbr] == 0 and np.random.random() < phi:
                        state_new[nbr] = 1
                        tot_infected_nodes += 1
    
        # Update the states
        for v in g.vertices():
            state_old[v] = state_new[v]
    
        # Update the time variable
        t += 1
        
    print("Total time required: ", ind, t)    
    f.write(str(ind) + ',' + str(t) + '\n') 
    
f.close()
