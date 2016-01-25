#!/usr/bin/env python
"""
This class implement EM algo to compute pathway expression

"""
__author__ = """ Blanche Temate"""
__date__ = "$Date: 11-05-2014 $"
__credits__ = """"""
__revision__ = "$Revision: 2 $"
#    Copyright (C) 2014 by 
#    TCB
#    All rights reserved.
#    BSD license.



import sys
import errno
import math

from Print_EM_Pathway import *



def printDict(dictGreen):
    for key, value in dictGreen.items():
        print (key,value)
        print

def print2Dict(dict1, dict2):
    for key, value in dict1.items():
        print (key,value, dict2[key])
        print
    
def createGreenMap ( SetofKoNames):
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


def initialize_pathway_express (greensDict) :
    initialDict = {}
    for pw in greensDict:
        initialDict[pw]= math.sqrt(len(greensDict[pw]))

    return  initialDict



def initialize_express_list (initialDict) :
    expr = {}
    
    for pw in initialDict:
        list_expr = []
        list_expr.append(initialDict[pw])
        expr[pw]= list_expr

    return  expr



def update_express_list (initialDict, expr1, expr2) :
    
    new_expr={}
    for pw in initialDict:
        list_expr = expr1[pw]
        list_expr.append( expr2[pw])
        new_expr[pw] = list_expr

    return  new_expr



def threshold_pathway (greensDict) :
    threshold = {}
    for pw in greensDict:    
        threshold[pw] = math.sqrt(len(greensDict[pw])) 

    return  threshold

                                      

def update_pathway_express (initialDict, greensDict, update_PW_Expr_Dict, protein_to_PW, threshold):
    update_expr = {}
    nberPWwithP = 0
    update = 0

    for pww in initialDict:
        for pr in greensDict[pww]:                                      
            for pw1 in protein_to_PW[pr]:
                if update_PW_Expr_Dict[pw1] >= threshold [pw1]:    #Question for Dr. Alex
                    nberPWwithP = nberPWwithP +1
            update = update + 1.0 / max(1, nberPWwithP)
            #print(" \n pathway: ", pw, " protein: ", pr," nberPWwithP: ", nberPWwithP)
            nberPWwithP =0
            

        update_expr[pww]=update
        update = 0
        
    return update_expr
    


def protein_participation (greensDict):
    protein_to_PW = {}
    values = set(a for b in greensDict.values() for a in b)
    protein_to_PW = dict((new_key, [key for key,value in greensDict.items() if new_key in value]) for new_key in values)

    return protein_to_PW



def step3 (update_PW_Expr_Dict1, update_PW_Expr_Dict2, epsilon):
    converge = True
    for pw in update_PW_Expr_Dict1:
        #print (pw, ": , update_PW_Expr_Dict2[pw] ", update_PW_Expr_Dict2[pw], "update_PW_Expr_Dict1[pw] ", update_PW_Expr_Dict1[pw])
        if abs(update_PW_Expr_Dict2[pw] - update_PW_Expr_Dict1 [pw]) > epsilon:
            converge = False
            break    
    return converge



##def step3 (pwDict, threshold):
##    passPW = []
##    for pw in pwDict:
##        if pwDict[pw] < 2.0*threshold[pw]: #pwDict[pw] < 2.0*threshold[pw]:
##            pwDict[pw] = 0
##        else:
##            passPW.append(pw)
##    
##    return pwDict, passPW



def main():
    #SetofKoNames = "C://Users//Charly//Dropbox//Projects//Bugula_Retina//EM//SetofKoNames_L1_Sep18.txt"
    SetofKoNames = "C://Users//Charly//Dropbox//Projects//Bugula_Retina//EM//SetofKoNames_L2_Oct6.txt"
    #SetofKoNames = "C://Users//temateb//Downloads//em//SetofKoNames_L2_Oct6.txt"
    #SetofKoNames = "C://Users//ytematetiagueu1//Dropbox//Projects//Bugula_Retina//EM//SetofKoNames_L2_Oct6.txt"
    #SetofKoNames = "C://Users//ytematetiagueu1//Dropbox//Projects//Bugula_Retina//EM//SetofKoNames_L1_Sep18.txt"    

    initialDict = {}
    greensDict = createGreenMap (SetofKoNames)
    protein_to_PW = protein_participation ( greensDict)    
    threshold = threshold_pathway (greensDict)

    print(" Start ")

    ########################## Step 1  ###########################################
    initialDict = initialize_pathway_express (greensDict)  #initialDict = step1()
    print(" \n initialDict ")
    #printDict(initialDict )
    
    ########################## Step 2  ###########################################    
##    update_PW_Expr_Dict = initialDict
##    update_PW_Expr_Dict1 = {}
##    for pw in update_PW_Expr_Dict:
##        update_PW_Expr_Dict1[pw] = update_pathway_express (pw, greensDict, update_PW_Expr_Dict, protein_to_PW,threshold)             

    expr_list = initialize_express_list (initialDict)

    epsilon = 0.01
    max_iter = 8
    counter = 0
    update_expr1 = initialDict
    update_expr2 = update_pathway_express (initialDict, greensDict, update_expr1, protein_to_PW, threshold)
    expr_list = update_express_list (initialDict, expr_list, update_expr2)

    print ("step3(update_expr1, update_expr2, epsilon)", step3(update_expr1, update_expr2, epsilon))
    while step3(update_expr1, update_expr2, epsilon)== False and max_iter >= counter :
     
        update_expr1 = update_expr2
        update_expr2 = update_pathway_express (initialDict, greensDict, update_expr1, protein_to_PW, threshold)
        expr_list = update_express_list (initialDict, expr_list, update_expr2)
        
        counter = counter + 1
        print(" counter", counter)

    #write_all_Expr (EM_name, greensDict, threshold, expr_list )
    print(" lenght expr_list: ", len(expr_list["ko05340"]))
    write_all_Expr ("with_epsilon_J07_L2", greensDict, threshold, expr_list )
    

    print("Finish")
    ##############################################################################
    # Tw = sqrt(|w|), Tw = 5, Tw = 8, Tw = 10.
    # Stopping criteria is the following: whenever the values stabilize or oscilate - stop.
    
main()                  



