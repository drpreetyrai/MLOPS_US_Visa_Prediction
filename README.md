
<img src="/Users/preetyrai/Desktop/MLOPS_US_VISA_Prediction/Screenshot 2025-04-04 at 8.42.51 PM.png" alt="Alt Text" width="full">

US Visa Approval Prediction 

Project Overview:
 * Undersstanding the Problem Statement 

 * Understanding the solution 

 * Code understanding & walkthrough 

 * Understanding the Deployment 



Deployment:
 * Docker 
 * Cloud Services 
 * Adding self hosted runner 
 * workflows 



Problme Statement:

US visa approval status

Given certain set of features such as (continent, education, job_experience, training, employment, current age etc .) 

We have to predict weather the application for the visa will be approved or not. 



Features:
Continent: Asia, Africa, North America, Europe, South America, Oceania 

Education: High Scool, Master's Degree, Bachelor's, Doctorate 

Job Experience: Yes, No

Required Training: Yes, No 
Number of employess: 15000 to 40000 
Region of employment: West, Northeast, South, Midwest, Island,

Prevailing Wage: 700 to 70000 

Contract Tenure: Hour, Year, Week, Month 

Full time : Yes, No

Age of company: 15 to 180 



Soluteion Scope:
This can be used on real life by US visa applicants so that they can improve their Resume and criteria for the approval process. 


Solution Approach:

1.) Machine Learning: ML Classification Algorithms 

2.) Deep Learning: Custom ANN with sigmoid activation Function 



# Solution Proposed 

We will be using ML
1.) Load the data from DB
2.) Perform EDA and feature engineering to select the desirable features. 
3.) Fit the ML classification Algorithm and find out which one performs better. 

4.) Select top few and tune hyperparameters.

5.) Select the bet model based on desired metrics.





Steps:- 

1.) First create template.py 




