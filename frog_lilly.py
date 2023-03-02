#!/usr/bin/python3.8

#    frog_lily.py: a solution for the classic problem presented by Christopher D. Long in https://twitter.com/octonion/status/1630687525567070213
#                  which consists in "Here's a classic. A frog is facing a line of 10 lily pads. 
#                                     With each jump, the frog moves forward, landing on one of 
#                                     the lily pads in front of it uniformly at random. 
#                                     What's the expected number of jumps required for the frog to reach the last lily pad?"

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

__author__ = "Josué P. J. de Freitas"
__license__ = "GPL"
__email__ = "josue.freitas@gmail.com"

#Original avaiable at https://github.com/josuepjfreitas/proba_random_stuff


import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

total_seasons_c = 10000
number_of_lilys_c = 10

list_results = [] 
random_position = 0
max_jump = number_of_lilys_c
total_jumps = 0
for i in range(total_seasons_c): #simulate for many seasons of jumps
    total_jumps = 0
    random_position = random.randint(1,max_jump) # first jump
    total_jumps += 1
    while random_position < number_of_lilys_c:
        random_position = random.randint(random_position+1,max_jump) #+1 because it will not jump in the same lily, just in one in front
        total_jumps += 1        
    list_results.append(total_jumps)     
    

print("Expected (most probable) number of jumps=",max(list_results,key=list_results.count)) 

occurrences = Counter(list_results)  

plt.bar(*zip(*occurrences.items()))
plt.show()

