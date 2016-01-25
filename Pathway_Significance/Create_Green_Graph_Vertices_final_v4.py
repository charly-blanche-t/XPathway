#!/usr/bin/env python
"""
This class create a green graph in memory representing KGML from KEGG
after analysis.

"""
__author__ = """ Blanche Temate"""
__date__ = "$Date: 4-29-2014 $"
__credits__ = """"""
__revision__ = "$Revision: 1 $"
#    Copyright (C) 2014 by 
#    TCB
#    All rights reserved.
#    BSD license.


import networkx as nx
import sys
import errno
import os.path
import os
import copy

from Create_KGML_Graph_final_v1 import *
from statistics_final_v3 import *
from combination_final_v2 import *
from significance_final_v3 import *


def printDict(dictGreen):
    for key, value in dictGreen.items():
        print (key,value)
        print


def printGraph(G):
    print(G.nodes())
    #List of all nodes without and with data
    print(G.nodes(data=True))
    # Similarly     # G.node # this is a dictionary of node attributes
    print(G.edges())



    
def createGreenMap ( SetofKoNames):
    # Step 1: Read the entire "green" file into a hashmap and keep it in memory
    # Create dictionary
    
    greens = {}

    fd = open(SetofKoNames)
    #ko00061 : K09458,K00645,K00059,K01961,K11262,K00665,

    for line in iter(fd):
        #print (line)
        words = line.split()
        green_nodes=[]
        green_nodes.extend(words[2].split(','))
        green_nodes.pop() 
        greens[words[0]]= green_nodes
        
    fd.close()

    return greens




def create_green_graph(g, mapDict):

    print

    graphName = (g.name).strip()
    words=[]
    if graphName in mapDict:           # test if the name of the group is a key in dict consisting of name of graph + green nodes
                                    # to make sure the "group" of that graph is effectively in the list of all map/k0/graph from the kegg website
        words = mapDict[graphName]     # words contains all the green nodes of this graph
       # print ("Name of the graph: ", graphName)

    for n in  g.nodes():

        for alias1 in g.node[n]['alias']:
            
            if alias1 in words:
                g.node[n]['color'] = 'green'
                #print ("Successful: node ", n , " is green")
                break
            else:
                g.node[n]['color'] = 'black'

    return g



def create_induced_green_graph (green, mapDict):

    graphName = (green.name).strip()
    words=[]
    error = 0
    H = nx.DiGraph()    
    
    if graphName in mapDict:  
        #G = green.to_undirected(reciprocal=False)
        G = green
        node_ss = [node for node, ndata in G.nodes(data=True) if ndata['color'] == 'green']
        H = G.subgraph(node_ss)
        #printGraph(H)
        if (len(H.nodes())<=3 or len(H.edges())<=3):
            error = 2
    else:
        error = 2

    return H, error





def main():

##    SetofKoNames ="C://Users//ytematetiagueu1//Dropbox//Projects//Bugula_Retina//Eclipse_Output//SetofKoNames1.txt"
##    dirname = "C://Qiong//Groups" # Contains all the network graph as text files

#    SetofKoNames ="C://Users//temateb//Qiong//SetofKoNames.txt"
#    dirname = "C://Users//temateb//Qiong//Groups" # Contains all the network graph as text files
    #dirname = "C://Users//temateb//Qiong//Groups_Copy" #

##    SetofKoNames ="C://Users//ytematetiagueu1//Dropbox//Projects//Bugula_Retina//Python//Files//SetofKoNames.txt"
##    dirname = "C://Users//ytematetiagueu1//Dropbox//Projects//Bugula_Retina//Python//Files//Group" # Contains all the network graph as text files

    SetofKoNames ="..//Files//SetofKoNames.txt"
    #dirname = "..//Files//Group" # Contains all the network graph as text files
    dirname = "../Files/Group3" #




##    SetofKoNames ="C://Qiong//SetofKoNames1.txt"
##    dirname = "C://Qiong//Groups" # Contains all the network graph as text files


    greensDict = createGreenMap (SetofKoNames)
    graphList=[]
    statDict = {}
    goodGraph =[]
	
    file_not_processed = 0
    file_for_dual = 0

    file_count = len([name for name in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, name))])

    #print ("file_count: ", file_count)
        
    for file in os.listdir(dirname):
        filename=dirname+"//"+file

        #print( "\nThe graph from", filename )
        print( "Processing graph from ", file )
        graph, error = create_graph(filename)  # From Create_KGML_Graph_v1 import *

        if error != 1:
            graphList.append(graph)

            green =  create_green_graph(graph, greensDict)      # graph (name=X) and greensDict(X:list of nodes)
            onlyGreen, error1 = create_induced_green_graph (green, greensDict)
            if (onlyGreen.number_of_nodes()>= (75*(green.number_of_nodes())/100)):
                error1 = 2
                goodGraph.append(graph.name)

            if error1 != 2:
                outputDict = create_stats (graph.name,green) # this should just be a list
                statDict = create_new_entry_statDict (graph.name, statDict, outputDict)
                
                outputDict = create_stats (graph.name,onlyGreen) # this should just be a list
                statDict = update_statDict  (graph.name, statDict, outputDict)
                
##                outputDict = create_stats (graph.name,onlyGreen) # this should just be a list
##                statDict = create_new_entry_statDict  (graph.name, statDict, outputDict)
                    

                copyOfGreen = copy.deepcopy(green)
                for i in range(200):
                    green_swapped = swap_vertices (copyOfGreen)

                    onlyGreen, error1 = create_induced_green_graph (green_swapped, greensDict)
                    outputDict = create_stats (graph.name,onlyGreen)
                    statDict = update_statDict (graph.name, statDict, outputDict)
                    copyOfGreen = green_swapped

            else:
                #print (" Cannot find map or wrong KO name: no green node detected")
                file_not_processed = file_not_processed +1
                               
        else:
            #print (" File requires dual graph !")
            file_for_dual = file_for_dual + 1


    print ( file_count - (file_not_processed + file_for_dual), " files were processed from a total of ", file_count, " files")
    print ( file_not_processed, " files do not have enough information and ", file_for_dual , " files require dual graph")
    write_goodGraph (goodGraph)
        

    pwPValue = all_P_Value(statDict)
    pwPValueReverse = all_P_Value_By_In_Out_deg(statDict) 
    #sys.exit(1)
    
    write_all_P_Value_V(pwPValue)
    write_all_P_Value_V_Reverse(pwPValueReverse)

    
    #write_centrality_vertices(statDict, "," )

    
##    writeDict_vertices(statDict, ",")
##    three_p_value_Dict = p_value (statDict)
##    #print ("three_p_value_Dict: ", three_p_value_Dict)
##    writeDensity_vertices(three_p_value_Dict)
    
main()





