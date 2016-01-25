
#!/bin/bash           

while read line
do           
    echo "$line"

    wget "http://www.kegg.jp/kegg-bin/download?entry=${line}&format=kgml" -O KoXML/${line}.xml
           

	./KGMLPathway2Graph/KGMLPathway2Graph KoXML/${line}.xml KoGrp/${line}

done <$1 
#done <ShortKoNames.txt


