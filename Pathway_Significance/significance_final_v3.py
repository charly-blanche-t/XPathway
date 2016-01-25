import copy
import operator
import csv
from array import *





def create_new_entry_statDict (graphName, statDict, outputDict):

    value = outputDict[graphName]

    density = []
    nodes = []
    edges = []
    centrality = []

    density.append(value[0])
    nodes.append(value[1])
    edges.append(value[2])
    centrality.append(value[3]) 


    list_of_arrays = []
    list_of_arrays.append(density)
    list_of_arrays.append(nodes)    
    list_of_arrays.append(edges)
    list_of_arrays.append(centrality)
    
    statDict[graphName]= list_of_arrays    

    return  statDict



def update_statDict (graphName,  statDict, outputDict):

    from_outputDict = outputDict[graphName]             #This is a list

    statDict[graphName][0].append(from_outputDict[0])   
    statDict[graphName][1].append(from_outputDict[1])
    statDict[graphName][2].append(from_outputDict[2])   
    statDict[graphName][3].append(from_outputDict[3])
    
    return  statDict



def create_new_entry_statDict1 (graphName, statDict, outputDict):

    value = outputDict[graphName]

    nber_green_cc = []
    nber_OneNode_cc = []
    nber_nodes_largest_cc =  []
    nber_edges_largest_cc =  []
    nber_edges_induced_graph =  []
    graph_density =  []
    
    nber_green_cc.append(value[0])
    nber_OneNode_cc.append(value[1])
    nber_nodes_largest_cc.append(value[2])
    nber_edges_largest_cc.append(value[3])
    nber_edges_induced_graph.append(value[4])
    graph_density.append(value[5])


    list_of_arrays = []
    list_of_arrays.append(nber_green_cc)
    list_of_arrays.append(nber_OneNode_cc)
    list_of_arrays.append(nber_nodes_largest_cc)
    list_of_arrays.append(nber_edges_largest_cc)
    list_of_arrays.append(nber_edges_induced_graph)
    list_of_arrays.append(graph_density)    

    statDict[graphName]= list_of_arrays
    

    return  statDict



def update_statDict1 (graphName,  statDict, outputDict):

    from_outputDict = outputDict[graphName]             #This is a list

    statDict[graphName][0].append(from_outputDict[0])   # This is an array statDict[graphName][0]
    statDict[graphName][1].append(from_outputDict[1])
    statDict[graphName][2].append(from_outputDict[2])
    statDict[graphName][3].append(from_outputDict[3])
    statDict[graphName][4].append(from_outputDict[4])
    statDict[graphName][5].append(from_outputDict[5])

    return  statDict




def write_centrality_vertices(statDict, sep):

    for i in statDict.keys():
        stat_filename = "Vertices/" + i + "_centrality_v.csv"

        with open(stat_filename, "w") as f:

            f.write("%s" % "Density")
            f.write(",")
            
            f.write("%s" % "#Nodes")
            f.write(",")

            f.write("%s" % "#Edges")
            f.write(",")

            f.write("%s" % "Centrality")
            f.write("\n")            

            for j in range (len (statDict[i][1])):
                f.write("%s" % statDict[i][0][j])
                f.write(",")
                f.write("%s" % statDict[i][1][j])
                f.write(",")
                f.write("%s" % statDict[i][2][j])
                f.write(",")
                f.write("%s" % statDict[i][3][j])
                f.write("\n")               


def write_centrality_edges(statDict, sep):

    for i in statDict.keys():
        stat_filename = "Edges/" + i + "_centrality_e.csv"

        with open(stat_filename, "w") as f:

            f.write("%s" % "Density")
            f.write(",")
            
            f.write("%s" % "#Nodes")
            f.write(",")

            f.write("%s" % "#Edges")
            f.write(",")

            f.write("%s" % "Centrality")
            f.write("\n")            

            for j in range (len (statDict[i][1])):
                f.write("%s" % statDict[i][0][j])
                f.write(",")
                f.write("%s" % statDict[i][1][j])
                f.write(",")
                f.write("%s" % statDict[i][2][j])
                f.write(",")
                f.write("%s" % statDict[i][3][j])
                f.write("\n")               




def write_all_P_Value_V (pwPValue):
    
    stat_filename = "Vertices/"  + "PValue_Vertices.csv"
    f = open(stat_filename, "wb") #Python 2.x
    #f = open(stat_filename, 'w', newline='') #Python 3.x
    fileWriter = csv.writer(f)
    fileWriter.writerow(['Pathway','Position','Density','#Nodes','#Edges','In/Out-Deg=0','Original#Nodes','Original#Edges']) #header row
    
    for i in pwPValue.keys():
        p = pwPValue[i]
        #print ("write i ", i, "  p", p)
        
        fileWriter.writerow([i, p[0],p[1],p[2],p[3],p[4],p[5],p[6]])
        
##        p = pwPValue[i]
##        #print ("write i ", i, "  p", p)
##        
##        if p<2:
##            fileWriter.writerow([ i, 1, 0, 0, p])
##        elif p<6:
##            fileWriter.writerow([ i, 0, 1, 0, p])
##        elif p<10:
##            fileWriter.writerow([ i, 0, 0, 1, p])
##        else:
##            fileWriter.writerow([ i, 0, 0, 0, p])




def write_all_P_Value_E (pwPValue):
    
    stat_filename = "Edges/"  + "PValue_Edges.csv"
    f = open(stat_filename, "wb") #Python 2.x
    #f = open(stat_filename, 'w', newline='') #Python 3.x
    fileWriter = csv.writer(f)
    fileWriter.writerow(['Pathway','Position','Density','#Nodes','#Edges','In/Out-Deg=0','Original#Nodes','Original#Edges']) #header row
    
    for i in pwPValue.keys():
        p = pwPValue[i]
        #print ("write i ", i, "  p", p)
        
        fileWriter.writerow([i, p[0],p[1],p[2],p[3],p[4],p[5],p[6]])




def write_all_P_Value_V_Reverse (pwPValue):
    
    stat_filename = "Vertices/"  + "PValue_Vertices_Reverse.csv"
    f = open(stat_filename, "wb") #Python 2.x
    #f = open(stat_filename, 'w', newline='') #Python 3.x
    fileWriter = csv.writer(f)
    fileWriter.writerow(['Pathway','Position','Density','#Nodes','#Edges','In/Out-Deg=0','Original#Nodes','Original#Edges']) #header row
    
    for i in pwPValue.keys():
        p = pwPValue[i]
        #print ("write i ", i, "  p", p)
        
        fileWriter.writerow([i, p[0],p[1],p[2],p[3],p[4],p[5],p[6]])



def write_all_P_Value_E_Reverse (pwPValue):
    
    stat_filename = "Edges/"  + "PValue_Edges_Reverse.csv"
    f = open(stat_filename, "wb") #Python 2.x
    #f = open(stat_filename, 'w', newline='') #Python 3.x
    fileWriter = csv.writer(f)
    fileWriter.writerow(['Pathway','Position','Density','#Nodes','#Edges','In/Out-Deg=0','Original#Nodes','Original#Edges']) #header row
    
    for i in pwPValue.keys():
        p = pwPValue[i]
        #print ("write i ", i, "  p", p)
        
        fileWriter.writerow([i, p[0],p[1],p[2],p[3],p[4],p[5],p[6]])


####################################################################################







def writeDict_vertices(statDict, sep):

    for i in statDict.keys():
        stat_filename = "Vertices/" + i + "_swap_vertices.csv"

        with open(stat_filename, "w") as f:

            f.write("%s" % "nberCC")
            f.write(",")
            
            f.write("%s" % "nberOneNodeCC")
            f.write(",")

            f.write("%s" % "highestNberNodesInCC")
            f.write(",")

            f.write("%s" % "highestNberEdgesInCCs")
            f.write(",")
            
            f.write("%s" % "nberEdgesInducedGraph")
            f.write(",")
            
            f.write("%s" % "density")
            f.write("\n")            

            for j in range (len (statDict[i][1])):
                f.write("%s" % statDict[i][0][j])
                f.write(",")
                f.write("%s" % statDict[i][1][j])
                f.write(",")
                f.write("%s" % statDict[i][2][j])
                f.write(",")
                f.write("%s" % statDict[i][3][j])
                f.write(",")                
                f.write("%s" % statDict[i][4][j])
                f.write(",")
                f.write("%s" % statDict[i][5][j])
                f.write("\n")               





def writeDict_edges(statDict, sep):
    
    for i in statDict.keys():
        stat_filename = "Edges/" + i + "_swap_edges.csv"

        with open(stat_filename, "w") as f:

            f.write("%s" % "nberCC")
            f.write(",")
            
            f.write("%s" % "nberOneNodeCC")
            f.write(",")

            f.write("%s" % "highestNberNodesInCC")
            f.write(",")

            f.write("%s" % "highestNberEdgesInCCs")
            f.write(",")
            
            f.write("%s" % "nberEdgesInducedGraph")
            f.write("\n")
            
            f.write("%s" % "density")
            f.write("\n")            

            for j in range (len (statDict[i][1])):
                f.write("%s" % statDict[i][0][j])
                f.write(",")
                f.write("%s" % statDict[i][1][j])
                f.write(",")
                f.write("%s" % statDict[i][2][j])
                f.write(",")
                f.write("%s" % statDict[i][3][j])
                f.write(",")                
                f.write("%s" % statDict[i][4][j])
                f.write(",")
                f.write("%s" % statDict[i][5][j])
                f.write("\n")               

                

            
