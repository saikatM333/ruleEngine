## **How to use**
 ### **step 1 - clone the project**
      git clone https://github.com/saikatM333/ruleEngine.git
 ### **step 2 - there are 2 setup project**
     1 -setup.sh for running the application is python is installed in the client device 
     2- setup-docker.sh for running the application in the docker 
 ## choose based on your prefrence 3.1 or 3.2 ##    
 ### **step 3.1 - If using `setup.sh`, the commands to be followed are:***
   
         chmod +x setup.sh
         ./setup.sh
     
  ### **step 3.2 - if using `setupDocker.sh`, command to be followed***
    
        chmod +x setup-docker.sh
        ./setupDocker.sh    
### **step 4 - now project is running in the port =8000**
use the example-json file to take the json body for each api end point

### ** Api endpoints **
 POST -  http://127.0.0.1:8000/api/rules/evaluate_rule
 POST - http://127.0.0.1:8000/api/rules/create_rule
 Post - http://127.0.0.1:8000/api/rules/combine_rules

