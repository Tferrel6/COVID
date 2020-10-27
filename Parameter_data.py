import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def Gaussian(sigma,mu,x_list):
	return 1./(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x_list - mu)**2 / (2 * sigma**2) )

def data_set(name):
	if name=="age": #age distribution
		#Taken from https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/
		age=np.arange(-87.5,90,5)
		female_dis=[9.57, 9.87, 10.18,10.31,10.57,11.5,11.08,10.85,10.01,10.31,10.39,11.23,10.71,9.26,7.53,5.33,3.64,4.23]
		male_dis=  [10.01,10.32,10.62,10.75,11.06,12,  11.35,10.88,9.91, 10.09,10.09,10.64,9.86, 8.2, 6.5, 4.32,2.68,2.38]
		return age,female_dis,male_dis

	elif name=="location":
		r_boundary=30. #30 miles boundary
		grid=0.1       #width of the grid
		sigma=2.       #2  miles radius city center
		mu=0    #[0,0] is the city center

		#From https://stackoverflow.com/questions/32208359/is-there-a-multi-dimensional-version-of-arange-linspace-in-numpy
		xy = np.mgrid[-r_boundary:r_boundary:grid, -r_boundary:r_boundary:grid].reshape(2,-1).T #even spaced grid in cartesian coordinates

		location=[]
		density=[]
		
		for coord in xy:
			[x, y]=coord
			r=(x**2.+y**2.)**(0.5)
			if r<=r_boundary:  #with in the boundary
				location.append([x, y])
				density.append(Gaussian(sigma,mu,r))
				
		return location,density