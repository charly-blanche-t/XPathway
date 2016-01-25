import copy
import operator
import csv
from array import *



def write_all_P_Value_V_Reverse (inputList, EM_name, update_PW_Expr_Dict, greensDict):
    
    #stat_filename = "Vertices/"  + "PValue_Vertices_Reverse.csv"
    em_result = "Output/" + EM_name  + ".csv"
    f = open(em_result, "wb") #Python 2.x
    fileWriter = csv.writer(f)
    fileWriter.writerow(['Pathway','Expression','#Proteins']) #header row

    for pw in inputList:
        fileWriter.writerow([pw, update_PW_Expr_Dict[pw],len(greensDict[pw]) ])



def write_all_Expr1 (EM_name, greensDict, threshold, expr_list ):
    
    em_result = "Output/" + "expre_list_last.csv"
    f = open(em_result, "wb") #Python 2.x
    #fileWriter = csv.writer(f)
    fileWriter = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # Get the length of one list in the dict
    # print("nber of pw expr computed ", len(expr_list.items()[0]))
    # use it to create colum header and to write each item
    # configure with length of list
    #fileWriter.writerow(['Expr1', 'Expr2', 'Expr3', 'Expr4', 'Expr5']) #header row

    for pw, expr in expr_list.items():
        fileWriter.writerow([[pw] + expr, threshold[pw]] )


def write_all_Expr (EM_name, greensDict, threshold, expr_list ):               
    #######################################################
    em_result = "Output/" + EM_name  + ".csv"
    f = open(em_result, "wb") #Python 2.x
    #fileWriter = csv.writer(f)
    fileWriter = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    fileWriter.writerow(['Pathway','#Proteins','Threshold','Expr1', 'Expr2', 'Expr3', 'Expr4', 'Expr5']) #header row

    for pw, expr in expr_list.items():
        fileWriter.writerow([pw ,len(greensDict[pw]), threshold[pw],  expr ])
               


##if sys.version_info >= (3,0,0):
##    f = open(filename, 'w', newline='')
##else:
    #f = open(filename, 'wb')

##    for pw in greensDict:
##        fileWriter.writerow([pw ,len(greensDict[pw]), threshold[pw], expr_list[pw] ])

