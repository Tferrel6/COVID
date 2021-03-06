import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#https://worldpopulationreview.com/states/georgia-population

def Gaussian(sigma,mu,x_list):
	return 1./(sigma * np.sqrt(2. * np.pi)) * np.exp( - (x_list - mu)**2. / (2. * sigma**2.) )

def norm_Gaussian(sigma,mu,x_list): #in quantum mech <psi 1| psi 1> = 1
	return 1./(np.pi**(0.25) * np.sqrt(sigma)) * np.exp( - (x_list - mu)**2. / (2. * sigma**2.) )

def cross_section(sigma1,mu1,sigma2,mu2):
	dx=0.01
	x_list=np.arange(-30,30,dx)
	cross_section_sum=np.sum(norm_Gaussian(sigma1,mu1,x_list)*norm_Gaussian(sigma2,mu2,x_list)*dx)
	return cross_section_sum

def distance_calc(location_list,location):
	distance_list=[]
	[x0,y0]=location
	for i in location_list:
		[x,y]=i
		r=((x-x0)**2.+(y-y0)**2.)**(0.5)
		distance_list.append(r)
	return distance_list

def data_set(name):
	
	if name=="age": #age distribution
		#Taken from https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/
		age=np.arange(-87.5,90,5)
		female_dis=[9.57, 9.87, 10.18,10.31,10.57,11.5,11.08,10.85,10.01,10.31,10.39,11.23,10.71,9.26,7.53,5.33,3.64,4.23]
		male_dis=  [10.01,10.32,10.62,10.75,11.06,12,  11.35,10.88,9.91, 10.09,10.09,10.64,9.86, 8.2, 6.5, 4.32,2.68,2.38]
		age_dis = np.hstack((np.flip(female_dis), male_dis))
		return age,age_dis

	elif name=="location":
		r_boundary=40. #30 miles boundary
		grid=0.1       #width of the grid
		sigma=3.       #2  miles radius city center
		mu=0    #[0,0] is the city center
		[x_center2,y_center2]=[20.,0.]

		#From https://stackoverflow.com/questions/32208359/is-there-a-multi-dimensional-version-of-arange-linspace-in-numpy
		xy = np.mgrid[-r_boundary:r_boundary:grid, -r_boundary:r_boundary:grid].reshape(2,-1).T #even spaced grid in cartesian coordinates

		location=[]
		density=[]
		
		for coord in xy:
			[x, y]=coord
			[x1, y1]=[x+x_center2, y+y_center2]
			r=(x**2.+y**2.)**(0.5)
			if r<=r_boundary:  #with in the boundary
				location.append([x, y])
				location.append([x1, y1])
				density.append(Gaussian(sigma,mu,r))
				density.append(0.2*Gaussian(sigma,mu,r))


		return location,density


	elif name=="infection_risk":
		female_dis=[0.4]*18
		male_dis=  [0.4]*18
		Infect_dis = np.hstack((np.flip(female_dis), male_dis))
		return Infect_dis
	elif name=="symptom":
		
		age_symptomatic_percent_female=[0,0.1,0.1,0.1,0.1,0.4,0.4,0.4,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.6,0.6,0.7] 	# 3 symptomatic
		age_symptomatic_percent_male  =[0,0.1,0.1,0.1,0.1,0.4,0.4,0.4,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.6,0.6,0.7]
		age_symptomatic_percent=np.hstack((np.flip(age_symptomatic_percent_female), age_symptomatic_percent_male))
		return age_symptomatic_percent

	elif name=="death_recover":
		death_recover_male  =[0,0.001,0.001,0.001,0.001,0.01,0.01,0.01,0.05,0.1,0.15,0.15,0.2,0.3,0.4,0.4,0.4,0.7] 	# male   1 death, 0 recover
		death_recover_female=[0,0.001,0.001,0.001,0.001,0.01,0.01,0.01,0.05,0.1,0.15,0.15,0.2,0.3,0.4,0.4,0.4,0.7]  	# female 1 death, 0 recover
		death_recover=np.hstack((np.flip(death_recover_female), death_recover_male))
		return death_recover



