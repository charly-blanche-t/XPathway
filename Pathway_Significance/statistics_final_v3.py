
#!/usr/bin/env python
"""
This class compute statistics from aor the induced green graph
"""
__author__ = """ Blanche Temate"""
__date__ = "$Date: 8-15-2014 $"
__credits__ = """"""
__revision__ = "$Revision: 1 $"
#    Copyright (C) 2014 by 
#    TCB
#    All rights reserved.
#    BSD license.


import networkx as nx
import sys
import operator





def create_stats (graphName, H):
  
    statDict = {}

    statsH = []
    if H.number_of_nodes()>1:
        density = float (H.number_of_edges())/  (float(H.number_of_nodes())-1)
        statsH.extend((density, H.number_of_nodes(), H.number_of_edges(), my_centrality(H) ))

    if H.number_of_nodes()<=1:
        print ("Impossible!!!")
        statsH.extend((0.0, 1, 0, 0.0))

    statDict[graphName]= statsH
    
    return statDict



def my_centrality(G):

    outdeg = G.out_degree()
    zero_out = [n for n in outdeg if outdeg[n] == 0]

    indeg = G.in_degree()
    zero_in = [n for n in indeg if indeg[n] == 0]

    connect2 = (float)(len(zero_out) + len(zero_in))/ (float)( 2 * G.number_of_nodes())

##    print ("zero-in :", zero_in)
##    print ("zero-out :", zero_out)
##    print ( "indeg: ", len(zero_in), "outdeg: ", len(zero_out), "nberNode: ",G.number_of_nodes() )
##
##    print ( "connect2: ", connect2)
    
    return connect2
        



def all_P_Value(statDict):

    pwPValue = {}
    
    for i in statDict.keys():
        
        pwList=[]
        original_item = (statDict[i][0][0], statDict[i][1][0],statDict[i][2][0],statDict[i][3][0])

        first_item = (statDict[i][0][1], statDict[i][1][1],statDict[i][2][1],statDict[i][3][1])

        for j in range (len (statDict[i][1])):
           pwList.append((statDict[i][0][j], statDict[i][1][j],statDict[i][2][j],statDict[i][3][j]))

        ##Sorting with Density descending (largest to smallest) and centrality ascending (smallest to largest)
        ## Stable sorting: sort by column a, b, c simply by sorting by comun c, then b, then a
           
        s = sorted(pwList, key = operator.itemgetter(3))
        s = sorted(s, key = operator.itemgetter(0), reverse=True)

        s.remove(original_item)  
        p = s.index(first_item)

##        print ("i ", i, " first item ",first_item)       
##        print ("index first item now", p)
        
        pwPValue[i]= (p,statDict[i][0][1], statDict[i][1][1],statDict[i][2][1],statDict[i][3][1], statDict[i][1][0],statDict[i][2][0])

    return pwPValue




def all_P_Value_By_In_Out_deg(statDict):

    pwPValue = {}
    
    for i in statDict.keys():
        
        pwList=[]
        original_item = (statDict[i][0][0], statDict[i][1][0],statDict[i][2][0],statDict[i][3][0])

        first_item = (statDict[i][0][1], statDict[i][1][1],statDict[i][2][1],statDict[i][3][1])

        for j in range (len (statDict[i][1])):
           pwList.append((statDict[i][0][j], statDict[i][1][j],statDict[i][2][j],statDict[i][3][j]))

        ##Sorting with Density descending (largest to smallest) and centrality ascending (smallest to largest)
        ## Stable sorting: sort by column a, b, c simply by sorting by comun c, then b, then a
           
        s = sorted(pwList, key = operator.itemgetter(0), reverse=True)
        s = sorted(s, key = operator.itemgetter(3))
##        s = sorted(s, key = operator.itemgetter(0), reverse=True)

        s.remove(original_item)  
        p = s.index(first_item)

##        print ("i ", i, " first item ",first_item)       
##        print ("index first item now", p)
        
        pwPValue[i]= (p,statDict[i][0][1], statDict[i][1][1],statDict[i][2][1],statDict[i][3][1], statDict[i][1][0],statDict[i][2][0])

    return pwPValue

    
