# National Hosiptal Readmission

![John's Hopkins Hospital](images/johns-hopkins-hospital.jpg)


## Background & Motivation

Medicare implemented the Hopital Readmissions Reduction Program (HRRP) which is a program that encourages hospitals to improve communication and care requirements to assist patients and caregivers in rehabilitation after being discharged, or realeased from the hospital. The 21st Century Cures Act directs the Centers for Medicare & Medicaid Services (CMS) to evaluate a hospital's readmission rate compared to hospitals with a similar proportion of patients eligible for Medicare and Medicaid benefits. 

There are six conditions/procedure-specific 30-day risk-standardized unplanned readmission measures in the program:
* Acute myocardial infarction (AMI)
* Chronic obstructive pulmonary disease (COPD)
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

My first questions when looking at this data was how readmission varied between the six conditions. To answer this I plotted the total number of readmissions over the number of discharges for each different condition. The results, shown below indicate that heart failure and chronic obstructive pulmonary disease have the highest readmission numbers compared to discharges. This indicates that perhaps there is room for improvement in the assistence for patients and caregivers being discharged for either of these two conditions. 
![Readmission for varying measures](images/readmission-for-varying-measures.png)

My second question was how readmission rate for coastal hospitals compared to non-coastal hospitals. There is a clear difference between the two, showing a significantly higher readmission rate for coastal hospitals. 

![Readmission for coastal v non-coastal](images/readmission-for-coast_v_noncoast.png)

The third and final exploratory question was how different states varied in readmission rate. 


## Hypothesis

This is a very large dataset with several hospitals in each state. There are many factors that may contribute to being readmitted to a hospital, and I wanted to know if those factors were influenced by being a hospital on the coast. I believe that population density is highest on the coasts, and in additon, many well-known universities, particularly for higher education in the medical field tend to be closer to the coasts. Based on this belief, I hypothesized that coastal hospitals would see a lower readmission rate. I suspected that many graduates of medical school would choose to remain located closer to where they graduated and therefore you would see more competition and better doctors on the coast, leading to a lower readmission rate. 

In order to test my hypothesis I set up a Bayesian A/B test, testing coastal versus non-coastal states. I defined my coastal states as any state with land touching the ocean, which led me to a list of 19 states. Variation A was coastal states, and variation B was non-coastal states. The first step was to come up with my priors, which I defined as P(VarA) = 1 and P(VarB) = 1. I then calculated my posterior parameters, and plotted my beta distribution. The final plot can be seen below, indicating that my hypothesis was incorrect, and that variation b - non-coastal states had a higher probability of 

![Readmission for Total](images/prob-readmission.png)

AMI (Heart Attack)
![Readmission for AMI](images/prob-ami-readmission.png)

COPD
![Readmission for COPD](images/prob-copd-readmission.png)

CABG
![Readmission for CABG](images/prob-cabg-readmission.png)

HF
![Readmission for HF](images/prob-hf-readmission.png)

HIP/KNEE
![Readmission for Hip/Knee](images/prob-hipknee-readmission.png)

PN
![Readmission for PN](images/prob-pn-readmission.png)



## Conclusion

## Citation




General Note: Have good organization, appropriate use of text and illustrations, helpful references, beautiful and well put together graphics.