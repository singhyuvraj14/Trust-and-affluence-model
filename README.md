Less than 10% Indians have a credit bureau presence, so it is essential to identify and utilize
alternate forms of data to assess customer’s credit worthiness. We want to identify markers from social media data that indicate trust and affluence;

Our results provide a new insight to improve risk control for lending in India On one hand, individuals in India do not have a well-verified credit score, such as FICO score, which enlarges the information asymmetry in Indian lending markets. On the other hand, about 90% of internet users in India have a social media account.

Our problem is best framed as Multiple linear regression (MLR), also known simply as multiple regression, is a statistical technique that uses several explanatory variables to predict the outcome of a response variable.


Tools and technologies used:

As we start the working model for this problem statement we have used technologies such as-
●Django
●Python
●HTML
●CSS
●SQL
●Jupyter notebook

A)Django: Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern. It is maintained by the Django Software Foundation
It is used in the project for back-end and integration for the whole workflow.

B)Python:Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. 
The whole project is designed in this programming language as django is used and it is easy to integrate machine learning models with the entire django framework with python.


C)HTML:The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript.
In this project we have used html to structure our front end for the user and integrated it in django to it on the local server http://127.0.0.1:8000/trust/.

D)CSS:Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.
It is used to design front-end user interfaces.

E)SQL:SQL is a domain-specific language used in programming and designed for managing data held in a relational database management system, or for stream processing in a relational data stream management system.
The database is used to store the data of the user and produce a final result for the client of which the affluence score is predicted.

F)Jupyter notebook:Jupyter is a project and community whose goal is to "develop open-source software, open-standards, and services for interactive computing across dozens of programming languages
It is used to develop a regression model in the development phase it is used to debug and train the model.


Workflow/solution statement

This project is divided into two major parts >
1.In the first part, we will conduct an EDA on an open source dataset. We used Python data science and data visualization libraries to explore the dataset’s variables(specifically social media variables ) interact with the output variable that is the score and understand the data’s structure, oddities, patterns and relationships and train and save a linear regression model using the dataset  

2.The second part of our project offers the consumption of our trained linear regression model using a simple front end where a borrower can input their data and find out their credit score 


Trust and affluence Prediction

Hypothesis

HYPOTHESIS 1. : Borrowers who voluntarily disclose their social media accounts on lending platform are less likely to default
For those borrowers who have disclosed their social media accounts, their social media information can be collected and used to predict their default probability and they are also less likely to default 

HYPOTHESIS 2 Borrowers who have a larger social network in the social media site are less likely to default and would have a higher score 
Borrowers who have a bigger social network within the social media site are less likely to
Default  Borrowers’ engagement refers to how much a borrower is involved in the sociaL
media site, such as how many posts a borrower submit or what percentage dialogues a
Borrower hosts or joins. It is closely related to the time and efforts a borrower invest
within the social media site. As these inputs are aimed to establish a good social image or good relationships with others

HYPOTHESIS 3. Social network solidity contains predictability of loan default.
Social network solidity contains predictability of loan default.When borrowers apply for
loans, they will prefer to disclose many sorts of contact information to the platform. The
more contact information the borrower provides, the more social information the platform
can control. In the event of default, the platform will have more channels to contact
collection, and therefore the information that the borrower cannot pay the loan on 
time is going to be communicated to his social network. Whether a person is honest is
of great significance to the maintenance of his social relationship

Variables
Input / Independent variables 

1.SocialMediaAccess : whether borrower has given access to their social media
2. Friends : The number of followers can be regarded as a proxy for the scope of borrowers’ social network in the Sina microblog site     
3.post this month : We use the number of post that the borrower has posted on his page as a measurement of his engagement in the social media site,


Control Variables 
Borrower’s credit characteristics. This set of control variables includes borrowers
1.LoanOriginalAmount  :  The origination amount of the loan.
2.2. StatedMonthlyIncome  :The monthly income the borrower stated at the time the listing was created.
3.Term:  The length of the loan expressed in months.      
4. EmploymentStatus  : The employment status of the borrower at the time they posted the listing.   
5.DebtToIncomeRatio  :   The ratio of debt to it’s income 
6.MonthlyLoanPayment  :The scheduled monthly loan payment.
7.IsBorrowerHomeowner: whether Borrower is homeowner or not



Output/Dependent Variable

The dependent variable is the trust and affluence score that we have assigned to the borrower according to the our explanatory variables 

Key Insights 
1.The loan original amount has many variations with maximum values in between 5000 to 15000 dollars and maximum loan original amount that has processed in this data is of 35000 and greater the loan asked the greater is the score observed because they are likely to receive less rate of interest on larger loans 
2.According to our hypothesis we can see that those who have given access to their social media have higher average prosper scores whereas those who have not given access have a lesser average  score
3.with more friends / bigger borrower social network credit score also is increased in the data 




Creating A User Interface for the borrower 
The aim is to create an easy to use interface for the user to calculate their trust and affluence score using their social media for that in this project a basic index page is created to provide information about our project and provide a button using which the user is redirected to another page where a basic HTML form takes in various input from the user. 

1.The Borrower's name 
2.The Loan Amount  
3.Monthly Income 
4.Social media access
5.Twitter username 
6.Employment status
7.Homeowner

Using this data when the submit button is clicked the data is extracted using django forms as a JSON file.
The Username is used to  is used to extract valuable information from the Twitter API , that is then stored in data frame along with the other user data which acts as an input to our trained linear regression model, 
The model gives a single numerical output and a trust and affluence score out of 1100 which is then shown to the user on the final page and the user data is stored in the MySQL database.
