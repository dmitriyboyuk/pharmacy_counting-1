# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def pharmacy_dictionary(input_file_path='input/itcont.txt'):
    
    #read text lines into a list
    with open(input_file_path) as file:
        lines = list(line.strip() for line in file)
    
    #define dictionary keys 
    dictionary = {'id':[], 'drug_name':[], 'drug_cost':[]}   

    #populate the dictionary by scraping info by line
    for line in lines[1:]:
        
        #strip inner quotes of delimiters if present  
        if line.find('"') != -1:         
            quote=[]            
            for index,text in enumerate (line): 
                if text == '"':
                    quote.append(index) 
            
            start = quote[0]
            end = quote[1]+1
            line = line[:start]+line[start:end].replace(',', '')+line[end:]
        
        #split line items and append to correspoding pharmacy dictionary keys  
        items = line.split(',')
        dictionary['id'].append('_'.join(items[0:3]))
        dictionary['drug_name'].append(items[3]) 
        dictionary['drug_cost'].append(items[4])                 
    
    return dictionary        
    



def top_cost_drug(input_file_path='input/itcont.txt', output_file_path ='output/top_cost_drug.txt'):
    
    #process pharmacy info into a dictionary 
    dictionary = pharmacy_dictionary(input_file_path)
    
    #list of unqiue drugs in pharmacy data  
    drug_name = list(set(dictionary['drug_name']))
    
    #obtain the number of unique prescribers and total cost per drug
    num_prescriber = []
    total_cost = [] 
    for drug in drug_name:    
    
        prescriber=[]
        cost=[]    
        for index,item in enumerate(dictionary['drug_name']):
            if item == drug:
                prescriber.append(dictionary['id'][index])
                cost.append(float(dictionary['drug_cost'][index]))
                
        num_prescriber.append(len(list(set(prescriber))))    
        total_cost.append(round(sum(cost),2))
    
    #combine and sort the 3 lists by total cost, highest first 
    output = sorted(zip(drug_name, num_prescriber, total_cost),  key = lambda x:x[2], reverse=True) 
    
    #add column labels for output
    header = ['drug_name','num_prescriber','total_cost']
    output.insert(0,header)
    
    #write to file 
    with open(output_file_path, 'w') as file:    
        for line in output:
            file.write('%s' % str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + '\n') 
          
                
if __name__ == '__main__':
    pharmacy_dictionary()
    top_cost_drug()







