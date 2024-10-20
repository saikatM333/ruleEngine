## **How to use**
 ### **step 1 - clone the project**
 ### **step 2 - there are 2 setup project**
     1 -setup.sh for running the application is python is installed in the client device 
     2- setup-docker.sh for running the application in the docker 
 ### **step 3 - make the script excutable, choose the commond based on the prefrence***
     1-chmod +x setup.sh
     2- chmod +x setup-docker.sh
### **step 4 - now project is running in the port =8000**
use the example-json file to take the json body for each api end point

### ** Api endpoints **
 POST -  http://127.0.0.1:8000/api/rules/evaluate_rule
 POST - http://127.0.0.1:8000/api/rules/create_rule
 Post - http://127.0.0.1:8000/api/rules/combine_rules

