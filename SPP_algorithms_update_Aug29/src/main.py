"""User interface for Shortest Path Algorithm Implementations

08/26/21, Alicia Tang (ftang12@asu.edu)

Modification:
    - Added function to get Connectivity Matrix: GetG() in utility_G.py
    - Added implementation of Floyd-Warshall Algorithm: CalculateAPSPFloyd() in spalgm_fw.py

"""

from utilities_G import ReadLinks, ReadNodes
from spalgm_fw import CalculateAPSP


ReadNodes('../data/node_Chicago.csv')
ReadLinks('../data/link_Chicago.csv')
CalculateAPSP('dij')
CalculateAPSP('fw')

print()


