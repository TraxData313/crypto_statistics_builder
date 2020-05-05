# Crypto Statistics Builder
Python AWS lambda that builds crypto price statistics and stores them in S3

# How to install:
- Create a lambda and upload the code from lambda.zip (this will upload all needed dependancies)
- - DETAILS:  to check the cbpro library dependancies. Create a folder with the cbpro
- Change the lambda code from lambda_function.py
...

## How to build the dependancies zip:
- Create an empty folder named "lambda" and add cbpro library with all its dependancies in it
- To find cbpro dependancies run "pip show cbpro"
- To find where the cbpro and the other libraries are run "python" -> "import cbpro" -> "cbpro.__file__" and you should get the location of the libraries like ">>> 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\cbpro\\__init__.py'"
- Copy the cbpro folder togather with its dependancies in the "lambda" folder and use 7-zip to create the "lambda.zip" file

