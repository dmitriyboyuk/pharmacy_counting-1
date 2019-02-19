# -*- coding: utf-8 -*-
''' 
 Author: Dmitriy Boyuk

 Pharmacy Counting - Inisght Data Engineering Program application

 Generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, 
 and the total drug cost, which must be listed in descending order based on the total drug cost 
 and if there is a tie, drug name in ascending order
'''

from collections import defaultdict

def pharmacy_dictionary(input_file_path='input/itcont.txt'):
    
    # read text lines into a list
    with open(input_file_path) as file:
        lines = list(line.strip() for line in file)
    
    # define dictionary 
    prescr_dictionary = defaultdict(list) 
    cost_dictionary = defaultdict(list) 

    # populate the dictionary by scraping info by line
    for line in lines[1:]:
        
        # strip inner quotes of delimiters if present  
        if line.find('"') != -1:         
            quote=[]            
            for index,text in enumerate (line): 
                if text == '"':
                    quote.append(index) 
            
            start = quote[0]
            end = quote[1]+1
            line = line[:start]+line[start:end].replace(',', '')+line[end:]
        
        # split line items and append to correspoding pharmacy dictionary keys  
        items = line.split(',')
      
        # dict with key=drug_name and value=[list of drug_cost]
        prescr_dictionary[items[3]].append('_'.join(items[1:3])) 
        
        # dict with key=drug_name and value=[list of prescribers]
        cost_dictionary[items[3]].append(float(items[4]))  
    
    return  prescr_dictionary, cost_dictionary        



def top_cost_drug(input_file_path='input/itcont.txt', output_file_path ='output/top_cost_drug.txt'):
    
    # process pharmacy info into a dictionary 
    prescr_dictionary, cost_dictionary = pharmacy_dictionary(input_file_path)
    
    final_list=[]
    for key in cost_dictionary:        
        # for each drug:
        # sum total cost across all prescriptions  
        s=round(sum(cost_dictionary[key]))
        
        # number of unqiue prescriber per drug 
        l=len(list(set(prescr_dictionary[key])))
        
        # concat drug_name, num_prescribers and drig_cost into a list
        final_list.append((key,l,s))
        
    # sort final list by first by cost (descending) and then by drug name (ascending)  
    sorted_final_list=sorted(final_list, key=lambda element: (-element[2], element[0]))           

    # add column labels for output
    header = ['drug_name','num_prescriber','total_cost']
    
    # write to file 
    with open(output_file_path, 'w') as file: 
        file.write('%s' % str(header[0]) + ',' + str(header[1]) + ',' + str(header[2]) + '\n') 
        for line in sorted_final_list:
            file.write('%s' % str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + '\n') 
    
      
                
if __name__ == '__main__':
    top_cost_drug()
        
  







