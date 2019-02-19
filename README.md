# Pharmacy Counting Challenge 

## Table of Contents
1. [Problem](README.md#problem)
1. [Input](README.md#input)
1. [Solution](README.md#solution)
1. [Output](README.md#output)
1. [Final Comments](README.md#final-comments)

## Problem 

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order 

## Input

The original dataset was obtained from the Centers for Medicare & Medicaid Services. It has been cleaned and simplified to match the scope of this coding challenge and is available <a href="https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view?usp=sharing">here</a>. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

A 5% random sample of the full dataset was pulled into the input repo directory to test the code using the `sample-test-input.py` script, which can be found in the `/src` directory 
 
## Solution 

1. Read the input text file by line and populate two dictionaries using drug names as keys:
    * drug : list of all the charges found for that drug 
    * drug : list of distinct prescribers
2. Sum total the cost across all prescriptions per drug using the drug:cost dictionary  
3. Count the number of unique prescribers per drug using the drug:prescribers dictionary
4. Sort the final list  - containing drug name, number of prescribers, and total_cost - in the order of descending total cost and then by drug name alphabetically incase of tie      

## Output 

The output file, `top_cost_drug.txt`, contains comma separated fields in each line as follows: 

drug_name,num_prescriber,total_cost

## Final Comments 

1. In my test directories `insight_testsuite/tests/my-own-test_1` and `insight_testsuite/tests/my-own-test_2`, executing `run.sh`:  
* First runs the `sample-test-input.py` script - pulling a 5% random sample from the main input file in the `input` directory   
* Then runs the `pharmacy-counting.py` script - processing the newly sampled data 

2. This repo structure **has been forked** from `InsightDataScience/pharmacy_counting` repo in order to pass the <a href="http://ec2-18-210-131-67.compute-1.amazonaws.com/test-my-repo-link">repo directory structure test</a> provided

My own cloned repo directory structure https://github.com/dmitriyboyuk/pharmacy_counting-master does not pass this test. This identical **non-forked** repo has also been shared with `insight-cc-bot` 

**Thank you for your time and consideration**

