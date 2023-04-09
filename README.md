# Python Gmail Birthday Greeting Bot  

Automatically greet your employees on their birthday!

System developed for We Plan S.A., a Business Intelligence Consultant Enterprise from Argentina.

## How It's Made:

**Tech used:** Python, HTML, Amazon Web Services, Task Automation

The system is programmed in Python language and is fed by a spreadsheet called "data_limpia.xlsx", which contains three columns: Name, Date of birth, and Email of We Plan employees.

The program is designed to go through the column with the birth dates, and if the current date matches any of the dates in the column, a congratulatory email is sent to all enterprise domain emails present in the Excel file.

These greetings are based on three HTML files, and for each greeting, one of the three is randomly selected. The program writes the employee's name in the greeting and sends the email.

Note that for the system to function correctly, the source code file (Python file), the Excel file, and the three HTML templates must be located in the same folder.

The system was deployed on the "WPGsrv01" virtual machine, an AWS server. Access is granted using the following credentials:

User: mbarreiro
Password: #######

The system's operation is ensured through the use of the Windows application "Task Scheduler," which schedules the execution of the Python code every day at 9 am.

The relevant files and access to the virtual machine can be found in the Drive folder where this same instruction manual is located.

## Optimizations

I consistently refactor and optimize my code, sometimes for efficiency, sometimes for readability.

## Lessons Learned:

The Biggest Lesson I learned in tackling this endless supply of questions is understanding that there is a long way to go. Not being able to answer a question is okay, as long as you take the initiative to improve.