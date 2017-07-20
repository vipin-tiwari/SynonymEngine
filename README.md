#Introduction
The Vagrantfile has been provided for the beta testing/
The Vagrantfile  configures the box with port-forwarding and provisions with:
 a. bootstrap.sh 
 b. run ansible playbook
 c. startup the application.

Please follow below steps:

1. vagrant up

# Start with the App Testing
2. GET Request: http://localhost:9000/<term>
   404 Error with : No synonym for term <term>

3. POST Request: http://localhost:9000/<term>/<synonym>
   
4. Again, GET Request for Above term: http://localhost:9000/<term>
   The response will be the synonym saved in the previous post call.

Example:

 1. http://localhost:9000/good
    404 Error with : No synonym for term good

 2. POST Request: http://localhost:9000/good/excellent

 3. http://localhost:9000/good
 	Response: excellent

