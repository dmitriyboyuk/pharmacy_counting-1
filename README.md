# pharmacy_counting-master

# Table of Contents
1. [Problem](README.md#problem)
1. [Input](README.md#input)
1. [Solution](README.md#solution)
1. [Output](README.md#output)
1. [Final Comments](README.md#final-comments)

# Problem 

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order 

# Input

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

Note, due to file size limitations, a 1% random sample input file is located in the input directory. The full input file is avaiulable <a href="https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view?usp=sharing">Here</a> 
 
# Solution 

1. Read the input text file by line and populate two dictionaries using drug names as keys:
    * drug : list of all the charges found for that drug 
    * drug : list of distinct prescribers
2. Sum total the cost across all prescriptions per drug using the drug:cost dictionary  
3. Count the number of unique precrisbers per drug using the drug:prescribers dictionary
4. Sort the final list  - containg drug name, number of precribers, and total_cost - in the order of descending total cost and then by drug name aplphabetically incase of tie      

# Output 

The output file, `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line as follows: drug_name,num_prescriber,total_cost

# Final Comments 

The random sample input test dataset in the `insight_testsuite/tests/my-own-test_1/input` test directory was created using the `sample-test-input.py` script which can found in the `insight_testsuite/tests/my-own-test_1/src` directory

In my-own-test directories, executing run.sh first pulls a random sample of 5 percent (user defined) of line from the input file in the main input directory, and then excecutes the `pharmacy-counting.py` script
