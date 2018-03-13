import matplotlib.pyplot as plt
import numpy as np

def draw_graph(rank_list_1,rank_list_2 ,len):
	# line 1 points
	x1 = []
	for va in range(1,len):
		x1.append(va)
	xyt=np.array(x1)
	
	# plotting the line 1 points 
	plt.plot(rank_list_1, label = "user 1")
	 
	# plotting the line 2 points 
	plt.plot(rank_list_2, label = "user 2")
	 
	# naming the x axis
	plt.xlabel('contests')
	# naming the y axis
	plt.ylabel('ranks')
	# giving a title to my graph
	plt.title('Rank compare graph')
	 
	# show a legend on the plot
	plt.legend()
	 
	# function to show the plot
	plt.show()
#f=[3,1]
#s=[1228,1158]
#draw_graph(f,s,2)