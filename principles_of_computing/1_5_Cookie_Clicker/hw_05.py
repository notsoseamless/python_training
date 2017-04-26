"""
Simulator for greedy boss scenario
"""

#import simpleplot
import math
#import codeskulptor
#codeskulptor.set_timeout(20)

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    
    # initialize necessary local variables
    current_day = 0
    current_savings = 0
    total_salary_earned = 0
    current_bribe_cost = INITIAL_BRIBE_COST
    current_salary = INITIAL_SALARY
    
    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        
        # check whether we have enough savings to bribe without waiting
        if current_savings > current_bribe_cost:
            days_to_next_bribe = 0
        else:
            time_to_next_bribe = (current_bribe_cost - current_savings) / float(current_salary)
            days_to_next_bribe = int(math.ceil(time_to_next_bribe))
        
        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
        current_day += days_to_next_bribe

        # update state of simulation to reflect bribe
        current_savings += days_to_next_bribe * current_salary
        current_savings -= current_bribe_cost
        total_salary_earned += days_to_next_bribe * current_salary
        current_bribe_cost += bribe_cost_increment
        current_salary += SALARY_INCREMENT

        # update list with days vs total salary earned for most recent bribe
        # use plot_type to control whether regular or log/log plot
        if plot_type == STANDARD:
            print 'linear math'
            days_vs_earnings.append((current_day, total_salary_earned))
        else:
            print 'log math'
            days_vs_earnings.append([math.log(current_day), math.log(total_salary_earned)])
        
   
    # q4 changes:
    # For the next three problems, we will consider the case when bribe_cost_increment == 1000. 
    # First, convert the output of greedy_boss() into Log/Log form by taking the logarithm 
    # of both current_day and the total salary earned using math.log() before they appended 
    # to the list days_vs_earnings.

    # The plot of the resulting graph approaches a straight line as the number of days increase. 
    # This observation signals that the function might be a polynomial function. 
    # Compute the slope of this line and round it to the nearest integer to estimate 
    # the degree of this polynomial.   
    
	'''
    q5
    Examine the output of the simulation greedy_boss(50, 1000). Note you accumulate enough savings 
    to pay a bribe once every 10 days. 
    '''
    
    return days_vs_earnings



def run_simulations():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = STANDARD
    #plot_type = LOGLOG
    days = 2000
    #inc_0 = greedy_boss(days, 0, plot_type)
    #inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    #inc_2000 = greedy_boss(days, 2000, plot_type)
#    simpleplot.plot_lines("Greedy", 600, 600, "days", "total earnings", 
#                          [inc_0, inc_500, inc_1000, inc_2000], False,
#                         ["Bribe increment = 0", "Bribe increment = 500",
#                          "Bribe increment = 1000", "Bribe increment = 2000"])
    simpleplot.plot_lines("G", 500, 500, "days", "total earnings", 
                          [inc_1000], False,
                         ["Bribe increment = 1000"])



#run_simulations()

result =  greedy_boss(150, 1000, True)
print result
#for num in range(len(result)-1):
#    print result[num+1][1] - result[num][1]

    
for data in result:
    print data
print
for data in result:
    print data[1]
    
#print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700), (37, 14700)]

#print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900), (36, 18600)]
    

