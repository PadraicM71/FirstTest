# pip install beecolpy
from beecolpy import abc



#-------------------------------------------------------------------
'''
#Step-by-step:
#Create object and set the solver parameters:
abc_obj = abc(function,
              boundaries,
              colony_size=40,
              scouts=0.5,
              iterations=50,
              min_max='min',
              nan_protection=True,
              log_agents=True)

#Execute algorithm: 
abc_obj.fit()

#Get solution obtained after fit() execution:
solution = abc_obj.get_solution()
'''
#---------------------------------------------------------------------


"""
    Obs.: Each time fit() was executed, the algorithm iterate 
    'iterations' times resuming from last fit() execution.
"""

"""
    Parameters
    ----------
    function : Name
        A name of a function to minimize/maximize.
        Example: if the function is:
            def my_func(x): return x[0]**2 + x[1]**2 + 5*x[1]
            
            Use "my_func" as parameter.


    boundaries : List of Tuples
        A list of tuples containing the lower and upper boundaries of 
        each dimension of function domain.
        
        Obs.: The number of boundaries determines the dimension of 
        function.

        Example: A function F(x1, x2) = y with:
            (-5 <= x1 <= 5) and (-20 <= x2 <= 20) have the boundaries:
                [(-5,5), (-20,20)]


    [colony_size] : Int --optional-- (default: 40)
        A value that determines the number of bees in algorithm. Half 
        of this amount determines the number of points analyzed (food 
        sources).
        
        According articles, half of this number determines the amount 
        of Employed bees and other half is Onlooker bees.


    [scouts] : Float --optional-- (default: 0.5)
        Determines the limit of tries for scout bee discard a food 
        source and replace for a new one.
            - If scouts = 0 : 
                Scout_limit = colony_size * dimension

            - If scouts = (0 to 1) : 
                Scout_limit = colony_size * dimension * scouts
                    Obs.: scouts = 0.5 is used in [3] as benchmark.

            - If scouts >= 1 : 
                Scout_limit = scouts

        Obs.: Scout_limit is rounded down in all cases.


    [iterations] : Int --optional-- (default: 50)
        The number of iterations executed by algorithm.


    [min_max] : String --optional-- (default: 'min')
        Determines if algorithm will minimize or maximize the function.
            - If min_max = 'min' : (default)
                Locate the minimum of function.

            - If min_max = 'max' : 
                Locate the maximum of function.


    [nan_protection] : Boolean --optional-- (default: True)
        If true, re-generate food sources that get NaN value as cost 
        during initialization or during scout events. This option 
        usually helps the algorithm stability because, in rare cases, 
        NaN values can lock the algorithm in a infinite loop.
        
        Obs.: NaN protection can drastically increases calculation 
        time if analysed function has too many values of domain 
        returning NaN.


    [log_agents] : Boolean --optional-- (default: True)
        If true, beecolpy will register, before each iteration, the
        position of each food source. Useful to debug but, if there a
        high amount of food sources and/or iterations, this option
        drastically increases memory usage.


    Methods
    ----------
    fit()
        Execute the algorithm with defined parameters.

        Obs.: Returns a list with values found as minimum/maximum 
        coordinate.


    get_solution()
        Returns the value obtained after fit() the method.

        Obs.: If fit() is not executed, return the position of
        best initial condition.


    get_status()
        Returns a tuple with:
            - Number of complete iterations executed
            - Number of scout events during iterations
            - Number of times that NaN protection was activated


    get_agents()
        Returns a list with the position of each food source during
        each iteration if "log_agents = True".

        Parameters
        ----------
        [reset_agents] : bool --optional-- (default: False)
            If true, the food source position log will be cleaned in
            next fit().
"""

"""
To find the minimum  of sphere function on interval (-10 to 10) with
2 dimensions in domain using default parameters:
"""

from beecolpy import abc

def sphere(x):
	total = 0
	for i in range(len(x)):
		total += x[i]**2
	return total

def my_func(x): return x[0]**2 + x[1]**2 + 5*x[1]
	
# abc_obj = abc(sphere, [(-10,10), (-10,10)]) #Load data
# abc_obj.fit() #Execute the algorithm


abc_obj = abc(sphere,
              [(-10,10), (-10,10)],
              colony_size=40,
              scouts=0.5,
              iterations=50,
              min_max='min',
              nan_protection=True,
              log_agents=True)

abc_obj.fit() #Execute the algorithm

#If you want to get the obtained solution after execute the fit() method:
solution = abc_obj.get_solution()
print(solution)

#If you want to get the number of iterations executed, number of times that
#scout event occur and number of times that NaN protection actuated:
iterations = abc_obj.get_status()[0]
scout = abc_obj.get_status()[1]
nan_events = abc_obj.get_status()[2]

#If you want to get a list with position of all points (food sources) used in each iteration:
food_sources = abc_obj.get_agents()

