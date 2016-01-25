	import java.io.BufferedReader;
	import java.io.BufferedWriter;

import java.io.FileReader;
	import java.io.FileWriter;

	import java.util.HashMap;
import java.util.HashSet;
	import java.util.Map;
import java.util.TreeSet;

	import java.util.Iterator;
import java.util.Set;
	/**
	 * This program 
	 * 
	 * @author ytematetiagueu1
	 *
	 */
	
	
public class KoNames {


		
	KoNames (String fname){
			filename = fname;
		}
	
	
	static String filename;
	
	
	Map createSetForKoNumbers (String filename){
		
		Map<String,Set<String>> map = new HashMap<String,Set<String>>();
		int nberKo=0; 
		
		try{
			 BufferedReader br = new BufferedReader(new FileReader(filename)); 
		  
			 String newKo,strLine;
			 
		  // http://www.kegg.jp/kegg-bin/show_pathway?@ko00073/reference%3dwhite/default%3d%23bfffbf/K13356/K13357
		//	 http://www.kegg.jp/kegg-bin/show_pathway?@ko00072/reference%3dwhite/default%3d%23bfffbf/K01641/K01640/K01027/K00626/K00019
		//	 http://www.kegg.jp/kegg-bin/show_pathway?@ko00073/reference%3dwhite/default%3d%23bfffbf/K13356
			
			  			  
			  while ((strLine = br.readLine()) != null)   {
				  //System.out.println(" whole line: " + strLine);
				  newKo = strLine.substring(42, 49);
				  
				  System.out.println(" print ko name: " + newKo);
				  //System.out.println(" print substring of ko nbers: " + strLine.substring(88));
				  
				  nberKo ++;
				  String[] tokens = (strLine.substring(88)).split("\\/");
			      
				  
			      // Create map2 : (key= readId , set<alignment>)
			      if (!map.containsKey(newKo)) {
			    	  Set<String> s = new HashSet<String>();
			    	  for (int i = 0; i<tokens.length; i++){
			    	    s.add(tokens[i]);
			    	  } 
				        map.put(newKo, s);
				        System.out.println("into map ko name2: " + newKo);
				      }
			     }
				
			   br.close();		  
		  
				}catch (Exception e){//Catch exception if any
					System.err.println("Error (in reading): " + e.getMessage());
					e.printStackTrace();
				}
		
		
		System.out.println(" Number of Ko is: " + nberKo + " Finished creating map of Ko ");
		return map;
	}
	
	/**
	 * write 3 files:
	 * First containing only ko numbers
	 * Second: ko Number and number of green nodes
	 * third Ko Number and set of associated green node in terms of Ko number
	 * @param filename
	 */
	
void writeKoFiles (Map map){
		
		try{
			   // Create file				
				FileWriter fstream1 = new FileWriter("SetofKoNames_Sep18.txt");
				BufferedWriter out1 = new BufferedWriter(fstream1);
	
				
				FileWriter fstream2 = new FileWriter("NberofGreen_Sep18.txt");
				BufferedWriter out2 = new BufferedWriter(fstream2);
				
				FileWriter fstream3 = new FileWriter("KoNames_Sep18.txt");
				BufferedWriter out3 = new BufferedWriter(fstream3);
				
				for(Object word : map.keySet()) {
					  String ko = word.toString();
					  System.out.println(" word  "+ ko); 
					  out3.write( ko +"\n");
					  
					  Set<String> s  = (Set)map.get(word);
					  out2.write( ko + " : " + s.size() + "\n");
					  out1.write( ko + " : ");
					  
					  Iterator itr = s.iterator(); 
					  while(itr.hasNext()) {
						  String element = (String)itr.next(); 
					      out1.write(element + ",");
					   }
					   out1.write("\n");
				 }					  
			
			out1.close();
			out2.close();
			out3.close();
		}catch (Exception e){//Catch exception if any
			System.err.println("Error (in writing ): " + e.getMessage());
			e.printStackTrace();
		}
		System.out.println(" Finished writing Ko different files "); 
	}
		
		public static void main(String[] args) {
			
			   long start = System.currentTimeMillis();

			   //filename = args[0];
			   filename = "C:/Users/ytematetiagueu1/Dropbox/Projects/Bugula_Retina/Scripts/All_KGML_URL_L1_Sep18.txt";
			   KoNames kn= new KoNames(filename);
			   Map mp = kn.createSetForKoNumbers(filename);
			   kn.writeKoFiles(mp);
			   
			   

			   long end = System.currentTimeMillis();
			   System.out.println("Running time "+ (end - start)/1000.0 +" s\n");

		} 
	}		