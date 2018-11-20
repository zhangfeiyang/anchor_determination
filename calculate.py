#!/usr/bin/env python
import math
from ROOT import *
pi = 3.141592654
def get_arch_area(theta,r): # calculate area of arch
	return 1./2*theta*r*r -  1./2*r*r*math.sin(theta)

def get_triangle_area(theta1,theta2,theta,r):

	chord = 2*r*math.sin((theta2-theta1)/2.0) 
	
	angle1 = theta1/2
	angle2 = (pi-theta1-theta2+2*theta)/2
	angle3 = (pi+theta2-2*theta)/2
	side = chord/math.sin(angle3)*math.sin(angle1)
	
	return 1./2*side*chord*math.sin(angle2)

def get_dead_area(theta1,theta2,theta,r):
		
	area1 = get_arch_area(theta1,r)	
	area2 = get_arch_area(theta2 - theta1,r)	
	area3 = get_arch_area(pi - 2*(theta2 - theta),r)	
	area4 = get_triangle_area(theta1,theta2,theta,r)
	return area1 + area2 + area3 + area4
 	
if __name__ == '__main__':

	f = TFile('test.root','recreate')	
	t = TNtuple('t','','t1:t2:area')
	
	for Theta1 in list(i for i in range(0,90)):
		for Theta2 in list(i for i in range(int(Theta1)+1,90)):
			t.Fill(Theta1,Theta2,get_dead_area(Theta1*pi/180,Theta2*pi/180,10.0/180*pi,17.7))
			#print(Theta1,Theta2,get_dead_area(Theta1*pi/180,Theta2*pi/180,10.0/180*pi,17.7))
	t.Write()
	
	f.Close()
