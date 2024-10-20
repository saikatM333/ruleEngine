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
     
  ### **step 3.2 - if using `setup-docker.sh`, command to be followed***
    
        chmod +x setup-docker.sh
        ./setup-docker.sh    
  ### ** Note : step 4 - it will ask secret Key ** ###
     for secret key just press the enter key it will automaticaly genearate it.      
     
### **step 5 - now project is running in the port =8000**
use the example-json file to take the json body for each api end point

### ** Api endpoints **
 POST -  http://127.0.0.1:8000/api/rules/evaluate_rule
 POST - http://127.0.0.1:8000/api/rules/create_rule
 Post - http://127.0.0.1:8000/api/rules/combine_rules


## Design Choices ##

### ** 1. Rule-based Evaluation Design: ** ###
Description: This approach allows users to define rules in a structured format (such as logical expressions). These rules are evaluated against provided data to determine if the conditions are met.
Application in the Project:
Users can define rules (e.g., age > 30 AND department = 'Sales').
These rules are then parsed into an AST for structured evaluation.
The system evaluates whether the provided data meets the conditions defined by the rules.
### ** 2. Declarative Programming:** ###
Description: Focuses on what should be done, rather than how it is done. This approach is often seen in rules engines where rules are defined declaratively, and the underlying system interprets and evaluates these rules.
Application in the Project:
Users specify conditions like age > 30 or department = 'Sales', and the system figures out how to evaluate them.
The rules are written in a format that describes the desired outcomes without detailing the evaluation process.
### ** 3. Abstract Syntax Tree (AST) Parsing: ** ###
Description: An AST represents the syntactic structure of expressions. It breaks down logical expressions into a tree structure that can be easily evaluated.
Application in the Project:
The rules are converted into AST structures where each node represents an operator (e.g., AND, OR) or operand (e.g., age > 30).
The evaluation function traverses this tree to compute the result.
### **4. RESTful API Design:** ###
Description: The application uses RESTful design principles for interacting with the endpoints. Each endpoint (create rule, evaluate rule, combine rules) follows standard HTTP methods (POST) and provides a structured request-response format.
Application in the Project:
POST requests allow users to create, evaluate, or combine rules, with clear separation of concerns between different endpoints.

### ** MVC (Model-View-Controller) Pattern: ** ###

Description: The MVC pattern separates the application into three main components:
Model: Represents the data and business logic. In this application, it would include the rules and evaluation logic.
View: The user interface that interacts with users. Although the application seems to focus on API endpoints, the concept of views can still apply if there is a front-end interacting with the API.
Controller: Handles user input and interacts with the model to perform actions. In this case, the Django views would serve as controllers that process incoming requests, validate data, and interact with the model to execute business logic.
Application in the Project:
The Django views are responsible for handling requests, parsing inputs, and returning responses based on the business logic implemented in models.
### ** RESTful Design: ** ###

Description: The application follows REST principles, where each endpoint corresponds to a specific resource or action and uses standard HTTP methods (e.g., POST for creating and evaluating rules).
Application in the Project:
Each API endpoint is designed to perform a specific action related to rules, adhering to RESTful conventions to make the API predictable and easy to use.
Chain of Responsibility:

Description: This pattern allows passing requests along a chain of handlers until one handles the request. It is particularly useful in scenarios where multiple rules need to be evaluated.
Application in the Project:
When evaluating rules, the system can process the AST nodes in a chain-like manner, where each node is responsible for evaluating a part of the expression and passing the result up the chain.
### ** Decorator Pattern: ** ###

Description: This pattern allows behavior to be added to individual objects dynamically without affecting the behavior of other objects from the same class. It is useful for adding functionalities, like logging or validation.
Application in the Project:
While not explicitly stated, if the application later requires adding features like logging or additional validation for rules, decorators can be used to wrap existing rule-processing functions.
