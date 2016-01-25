Pathway tools to infer metabolic pathway activity level and significance

Java code: KoNames.java
To Download all ko names.
Input: output from Link Gopher containg "All KGML URL". Those url contain the green nodes representing mapped enzymes.
eg. ko00450
    ko00100


shell script: koDownload.sh 
To Download all kgml xml file.
The code call KGMLPathway2Graph program to downlad and directly convert kgml xml
files to graph ( nodes + vertices).
The script takes as input a text file containing Ko names and output graph.


Python scripts:
1- EM: New_EM_Integral_TwMult_epsilon.py
To compute pathway expression.
The main code above will compute expression level of pathway with input a text files contining pathways along with their particpating enzymes (ko numbers)

2: Pathway significance: Create_Green_Graph_Vertices_final_v4.py or Create_Green_Graph_edges_final_v4.py
The main class generate original and random green graph in memory representing KGML from KEGG. Those graph are then analyzed for their significance.
Input: set of ko names for green nodes along with all the pathways or network graphs as text files (these are referred as groups from KGMLPathway2Graph)
