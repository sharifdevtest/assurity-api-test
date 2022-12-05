# **Sample API : Acceptance Test Script**  
> _Python project_ 

Simple test script to verify the below mentioned acceptance criteria using the Assurity provided [Sample API](https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false)

<br>

### **Acceptance Criteria** 
---
- Name = "Carbon credits"
- CanRelist = true
- The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"

<br>

### **Installation / Getting started** :
---
1. [Download](https://git-scm.com/downloads) and install Git 
2. [Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) Git
2. [Download](https://www.python.org/downloads/) and install Python 3.0+
3. Install dependent/required python modules
    <br> `pip install -r requirements.txt`
    <br> 
    <br> This will install below modules :
    <br> **requests** - This allows you to send HTTP requests using Python
    <br> **pytest**   - Pytest is a python testing framework
 

<br>

### **Download project and execute** : [assurity-api-test](https://github.com/sharifdevtest/assurity-api-test)
---
1. Create folder of your choice on your local machine which will be your workspace 
2. Open cmd/terminal 
3. Go to your workpace folder
    <br> `cd <workspace_folder>`
    <br>
4. Clone/download project
    <br> `git clone https://github.com/sharifdevtest/assurity-api-test.git`
    <br> 
    
5. Go to the project folder 
    <br> `cd assurity-api-test`
    <br> 
6. Run the acceptance tests with below command 
    <br> `pytest -v .`
    <br><br> 
   

### **Execute negative test** : Optional
---
- Edit **_test_assurity_sample_api.py_** and incorporate invalid data for negative testing  
    <br>
    1.  Negative <u> **test_status_code** </u> : 
    <br><br> Change Line 20 : 
    <br> `URL = "https://api.tmsandbox.co.nz/v1/Categories/627/Details.json?catalogue=false"`
    <br><br> Run command :  `pytest -v .`
    <br><br>

    2.  Negative <u> **test_name** </u> : 
    <br><br> Change Line 30 :
    <br> `assert response_body['Name'] == "Carbon credits1", "Name is invalid, got {}".format(response_body['Name'])`
    <br><br> Run command :  `pytest -v .`
    <br><br>
   
    3.  Negative <u> **test_can_relist** </u> : 
    <br><br> Change Line 34 :
    <br> `assert response_body['CanRelist'] == False, "CanRelist is not True"`
    <br><br> Run command :  `pytest -v .`
    <br><br>
   
    4.  Negative <u> **test_promotion_gallery** </u> : 
    <br><br> Change Line 40 :
    <br> `if element['Name'] == "Gallery1":`
    <br><br> Run command :  `pytest -v .`
    <br><br>

    5.  Negative <u> **test_promotion_gallery_description** </u> : 
    <br><br> Change Line 41 :
    <br> `assert element['Description'] == "Good position in category1"`
    <br><br> Run command :  `pytest -v .`
    <br><br>

