"""
Soluton for "Plotting a distribution" for Further activities

Desktop solution using matplotlib
"""

import random
import matplotlib.pyplot as plt

def plot_dice_rolls(nrolls):
    """
    Plot the distribution of the sum of two dice when they are rolled
    nrolls times.

    Arguments:
    nrolls - the number of times to roll the pair of dice

    Returns:
    Nothing
    """

    # initialize things
    rolls = {}
    possible_rolls = range(2, 13)
    for roll in possible_rolls:
        rolls[roll] = 0   

    # perform nrolls trials
    for _ in range(nrolls):
        roll = random.randrange(1, 7) + random.randrange(1, 7)
        rolls[roll] += 1

    # Normalize the distribution to sum to one
    roll_distribution = [rolls[roll] / float(nrolls) 
                         for roll in possible_rolls]

    # Plot the distribution with nice labels
    plt.plot(possible_rolls, roll_distribution, "bo")
    plt.xlabel("Possible rolls")
    plt.ylabel("Fraction of rolls")
    plt.title("Distribution of rolls for two six-sided dice")
    plt.show()
    
plot_dice_rolls(10000)

