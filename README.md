# Student Test Calculator

![Student Test Calculation Heroku App](/assets/images/student_test_calc_ranking_table_from_herokuapp.PNG)

[Student Test Calculation Heroku App](https://student-test-calculator.herokuapp.com/)

# Introduction

Teachers put a lot of time into giving students correct and fair grades. The time spend for this task consume time that could be spent on planning inspiring classes, and other activities more focusing the main task to teach students. To reduce time for teachers calculating students test performance and in the end give fair grades, this applicant can support this process. Intention with application is to add basic test input as subject and max result and in the next step add students and their test result. The student test calculator application will calculate each student performance and assign grade according to pre-defined grade levels.

# UX

## User Stories

As a teacher:
- I would like to spend less time in matching student result to grade
- I would like to have an easy interface to give general test input as subject and max result
- I would like to add student by name and their test result
- I would like the student test performance to automatically be calculated
- I would like student performance to be matched with pre-defined grade levels and be given a grade

As an app developer:
- I would like users to have a easy to understand interface
- I would like the application to be intuitive
- I would like the application to manage typos with a dialogue question back to the user

## Design
No front-end development has been performed. Application run within the framework of Heroku and the output is presented in a performance sorted table. Some minor terminal styling was added to highlight the students who failed the test. As well sorting on performance was applied to rank students based on their test performance.

## Structure
Functional flow diagram was created to understand different challenges and functions needed to support the development of application

![student test calc flow diagram](/assets/images/student_test_calc_function_flowdiagram.PNG)

# Features

## Functions
- get_test_subject(): Function to get input from user about test subject

- get_max_test_result(): Function to get input form user about test max result for the purpose of calculating student performance: Validation added to secure right format of input given by user.

- add_student_result(max_result): Function to get input from user about student name and test result. Validation added to secure right format is given by user and that the student test result is nog more than the test max result.

- calc_student_performance(stud_data, max_result): Function to use the student test result and test max result to calculate performance and set test grade based on pre-defined grade levels. Converts the dictionary to list structure and append student list to student list of lists.

- list_data_to_table(stud_list_of_list): Function to convert the list to a table for improved visualization and adding column sorting on student performance providing a ranking view of the test result.

## Development planned for next increment
- add functionality to insert data to database
- add functionality to do trend analysis on student performance history

# Testing

## Manual Test
Manual tests have been performed according to below test cases. One bug was identified with regards to data type for student result impacting the possibility to give half points. This was corrected and validated.

![Manual test cases](/assets/images/student_test_calc_test_cases.PNG)

## pep8 test
Python code validation was done using pep8 (http://pep8online.com/). Running the code resulted in recommendations were provided about phyton best practice.

![pep8 test result](/assets/images/pep8_test_student_test_calc.PNG)

All except two notifications about E501 (line too long (99 > 79 characters), line too long (97 > 79 characters)) where handled as the proposed action resulted in new notification E128 (Continuation line under-indented for visual indent). Deviation from pep8 standard was accepted.

# Deployment

## Heroku deployment steps
1. Navigate to [Heroku](heroku.com) and Create an account if not yet available
2. Create New app with unique name and select a region
3. In the Menu bar navigate to settings and add Config Vars "PORT 8000"
4. Add buildpacks in this order:
   - heroku/python
   - heroku/nodejs
5. In the Menu bar navigate to Deploy and select GitHub as deployment method
6. Chose Automatic or Manual deploy, this project was deployed Manual "Main branch"

![Heroku deployment overview](/assets/images/heroku_student_test_calc_overview.PNG)

## Clone and run locally

### Clone by using GitHub repository URL

1. navigate to GitHub repository for [student_test_calc](https://github.com/EvergSwe/Calculate-Test-Result)
2. In the Menu Navigate to "CODE"
3. Select HTTPS and Copy URL
Open PyCharm (or prefered IDE)
4. select Get from VCS
5. Either chose Repository URL and past the URL and clone or chose GitHub and authenticate to your GitHub repository. Select repository to clone.
6. Repository is downloaded to local folder
7. check main file settings python interpreter if required packages are installed


# Credits

## Code
- Code inspirations has been picked up from variouse sources
  - Code institute Love-Sandwiches Project and course tutorials
  - https://www.geeksforgeeks.org/python-programming-language/
  - https://www.w3schools.com/python/
  - https://realpython.com/
  - https://www.freecodecamp.org/learn/data-analysis-with-python/
  - https://www.educba.com/python-validation/
  - https://pythonfusion.com/table-on-console-python/

  # Disclamer
  This project is for education purpose only


