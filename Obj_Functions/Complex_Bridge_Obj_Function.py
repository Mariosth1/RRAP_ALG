# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:37:55 2020

@author: Mariosth1
"""
"----------- Complex Bridge bjective Function Calculation -------------------"
"""
This is a function that will generate the total reliability in every iteration.

******************************************************************************    
*** This objective Function represents the Series System Problem**************
******************************************************************************    

r for component reliability in subsystem and n for the number of components
in a subsystem ... note that all components in a subsystem are of equal 
reliability.    
H is the constrain handling function
"""
import numpy as np

subsystems = 5
redundancy = 5
# lower_bound = 0.5
# upper_bound = 1
v = np.array([1.0, 2.0, 3.0, 4.0, 2.0])
w = np.array([7.0, 8.0, 8.0, 6.0, 9.0])
a = np.array([2.33, 1.45, 0.541, 8.05, 1.95]) * 10 ** (-5)
b = np.array([1.5, 1.5, 1.5, 1.5, 1.5])
T = 1000.0
v_bound = 110.0
w_bound = 200.0
c_bound = 175.0

def obj_function(r, n):
    from Obj_Functions.Penalty_Function import H_penalty

    R = (1 - (1 - r) ** n)

    solution_quality = (R[0][4] * (1 - (1 - R[0][0]) * (1 - R[0][2])) * \
                        (1 - (1 - R[0][1]) * (1 - R[0][3])) + (1 - R[0][4]) * \
                        (1 - (1 - R[0][0] * R[0][1]) * (1 - R[0][2] * R[0][3])))* \
                       H_penalty(r, n, v, w, a, b, T, v_bound, w_bound, c_bound)

    return solution_quality
