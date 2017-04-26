"""
Cookie Clicker Simulator

JRO 27/06/2015

"""

import simpleplot
import math


# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        '''
        init method
        '''
        # The total number of cookies produced throughout the entire game 
        self._cookie_total = 0.0      
        # The current number of cookies you have
        self._cookies = 0.0
        # The current time (in seconds) of the game
        self._time = 0.0
        # The current CPS "cookies per second"
        self._cps = 1.0
        # history list
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return 'Time: ' + str(self._time) + ' Current Cookies: ' + str(self._cookies) + ' CPS: ' + str(self._cps) + ' Total Cookies: ' + str(self._cookie_total)
        
    def get_cookies(self):
        """
        Return current number of cookies (not total number of cookies)
        """
        return self._cookies
    
    def get_total_cookies(self):
        """
        Return total cookies
        """
        return self._cookie_total
    
    def get_cps(self):
        """
        Get current CPS
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time
        """
        return self._time
    
    def get_history(self):
        """
        Return history list
        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)        
        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)
        Should return a float with no fractional part
        """
        #print 'time until', math.ceil(cookies / self._cps)
        if cookies < self._cookies:
            # we already have enough
            return 0.0
        else:
            return math.ceil((cookies - self._cookies) / self._cps)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state
        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._time += time
            new_cookies = self._cps * time
            self._cookies += new_cookies
            self._cookie_total += new_cookies
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state
        Should do nothing if you cannot afford the item
        """
        if cost <= self._cookies:
            self._cookies -= cost
            self._cps += additional_cps
            self._history.append((self._time, item_name, cost, self._cookie_total))

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    # clone the build_info object
    info = build_info.clone()
    # create a new ClickerState object    
    clicker = ClickerState()
    
    # Loop uintil ClickerState object reaches the duration of the simulation.
    while clicker.get_time() <= duration:
        
        # Check the current time and break out of the loop if the duration has been passed.
        time_now = clicker.get_time()
        if time_now > duration:
            print 'breaking from loop'
            break
        time_left = duration - time_now
        
        # Call the strategy function with the appropriate arguments to determine which 
        # item to purchase next. If the strategy function returns None, you should break
        # out of the loop, as that means no more items will be purchased.  
        # strategy(cookies, cps, history, time_left, build_info):
        next_item = strategy(clicker.get_cookies(), clicker.get_cps(), clicker.get_history(), time_left, info)
    
        if next_item == None:
            print 'no next items'
            break

    
        # Determine how much time must elapse until it is possible to purchase the item.
        time_to_save = clicker.time_until(info.get_cost(next_item))      
        
        # If you would have to wait past the duration of the simulation to purchase the 
        # item, you should end the simulation.
        if time_to_save > time_left:
            print 'no time to save', time_to_save, 'time left', time_left
            break
        
        # Wait until that time.
        clicker.wait(time_to_save)
    
        # Buy the item
        clicker.buy_item(next_item, info.get_cost(next_item), info.get_cps(next_item))
    
        # Update the build information.
        info.update_item(next_item)
        
    # any time left then use it to make more cookies
    time_left = duration - clicker.get_time()
    if time_left:
        print 'we have', time_left, 'left'
        clicker.wait(time_left)
        
    return clicker


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    # get list of available items
    items = get_build_items(build_info)
    # sort keys by price
    sorted_items = sorted(items, key=lambda k: items[k][0])
    cheapest = sorted_items[0]
    if ((time_left * cps) + cookies) >= build_info.get_cost(cheapest):
        return cheapest
    else:
        return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    # get list of available items
    items = get_build_items(build_info)
    # sort keys by price
    sorted_items = sorted(items, key=lambda k: items[k][0], reverse=True)
    print sorted_items
    # choose most expensive we can afford
    for sorted_item in sorted_items:
        if ((time_left * cps) + cookies) >= build_info.get_cost(sorted_item):
            return sorted_item
    # nothing we can afford
    return None


def strategy_lo_cps(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    # get list of available items
    items = get_build_items(build_info)
    # sort keys by price
    sorted_items = sorted(items, key=lambda k: items[k][1])
    lo_cps = sorted_items[0]
    if ((time_left * cps) + cookies) >= build_info.get_cost(lo_cps):
        return lo_cps
    else:
        return None



def strategy_hi_cps(cookies, cps, history, time_left, build_info):
    """
    Always buy the highest CPS item you can afford in the time left.
    """
    # get list of available items
    items = get_build_items(build_info)
    # sort keys by cps
    sorted_items = sorted(items, key=lambda k: items[k][1], reverse=True)
    # choose most expensive we can afford
    for sorted_item in sorted_items:
        if ((time_left * cps) + cookies) >= build_info.get_cost(sorted_item):
            return sorted_item
    # nothing we can afford
    return None


def strategy_bfb(cookies, cps, history, time_left, build_info):
    """
    Always buy the highest bang for buck item you can afford in the time left.
    """
    # get list of available items
    items = get_build_items(build_info)
    # sort keys by cps
    sorted_items = sorted(items, key=lambda k: items[k][0] / items[k][1])
    # choose most expensive we can afford
    for sorted_item in sorted_items:
        if ((time_left * cps) + cookies) >= build_info.get_cost(sorted_item):
            return sorted_item
    # nothing we can afford
    return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    # get list of available items
    items = get_build_items(build_info)
    # sort keys by cps
    sorted_items = sorted(items, key=lambda k: items[k][0] / items[k][1])
    # choose most expensive we can afford
    for sorted_item in sorted_items:
        if ((time_left * cps) + cookies) >= build_info.get_cost(sorted_item):
            return sorted_item
    # nothing we can afford
    return None


def get_build_items(build_info):
    '''
    helper returns a calatogue like in build info
    '''
    info = {}
    for item in build_info.build_items():
        info[item] = (build_info.get_cost(item), build_info.get_cps(item))
    return info

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state
    print '(time, item, cost of item, total cookies)' 
    print
    print state
    
    # Plot total cookies over time
    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    #run_strategy("Cursor", SIM_TIME, strategy_none)
    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("hi_cps", SIM_TIME, strategy_hi_cps)
    #run_strategy("lo_cps", SIM_TIME, strategy_lo_cps)
    #run_strategy("bfb", SIM_TIME, strategy_bfb)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    

run()


    



