# National Hosiptal Readmission

## Background & Motivation

Medicare implemented the Hopital Readmissions Reduction Program (HRRP) which is a program that encourages hospitals to improve communication and care requirements to assist patients and caregivers in rehabilitation after being discharged, or realeased from the hospital. The 21st Century Cures Act directs the Centers for Medicare & Medicaid Services (CMS) to evaluate a hospital's readmission rate compared to hospitals with a similar proportion of patients eligible for Medicare and Medicaid benefits. 

There are six conditions/procedure-specific 30-day risk-standardized unplanned readmission measures in the program:
* Acute myocardial infarction (AMI)
* Chronic ovstructive pulmonary disease (COPD)
* Heart failure (HF)
* Pneumonia
* Coronary artery bypass graft (CABG) surgery
* Elective primary total hip arthroplasty and/or total knee arthroplasty (THA/TKA)

I became interested in the rates at which hospitals are readmitting patients from watching my aunt and uncle struggle with intense cargiving plans after being discharged from the hospital and seeing my uncle be readmitted to the hospital repeatedly. I wanted to know how readmission varied over the country and through different hospitals. 


## The Data

The federal government has a website, managed by the Centers for Medicare & Medicaid Servies, that provides a large dataset of 3,224 hospitals nation-wide. It lists metrics for discharge (being released from the hospital) and readmission (being readmitted to the hospital) for each of the six conditions that had high risk of re-admission, mentioned previously. Some of the key features that I used to analyize the data were facility name, state, measure, number of discharges, and number of readmissions. The data was collected over a three-year period from July 1st 2015 to June 30th 2018.

## Data Cleaning

While looking at the data, I noticed that there were several missing rows for number of discharges and number of readmissions. I also realized, upon further analysis that what I initially thought to be integers were actually strings. So my first actions were to convert non-numbers in the 'Number of Discharges' and 'Number of Readmissions' to zero, and to make sure these rows were all integers rather than strings so that I could start expoloring my data. 

## Exploratory Data Analysis

My first questions when looking at this data was how readmission varied between the six conditions.


My second question was how actual discharge rate compared to expected discharge rate between hospitals.

The third and final exploratory question was how different states varied in readmission rate. 


## Hypothesis
Clearly explain hypothesis testing. Make sure it is suited for the problem. Explain approach/method and thoroughly explain and walk through the hypothesis test.

## Conclusion

## Citation



General Note: Have good organization, appropriate use of text and illustrations, helpful references, beautiful and well put together graphics.