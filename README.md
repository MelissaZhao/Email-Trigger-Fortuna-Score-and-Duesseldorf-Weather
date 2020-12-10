### Email Trigger: Fortuna-Düsseldorf score and Düsseldorf weather

####  Topic: 
The theme of this project aims to send the regular Email to football fan of Fortuna-Düsseldorf club about the football score of Fortuna and the weather in Düsseldorf on that day.

####  Structure: 
The project is mainly divided into six parts.

1. The first part uses Beautiful Soup to parse and extract the weather information of Düsseldorf from the weather forecast website.

2. The second part utilise Pandas to obtain the information of the Fortuna's game score in tabular form from kicker.de webpage , and convert and save it as a local csv file.

3. The third part is to create a SQL database, and insert the content of the updated columns from local csv file into the sql tabel for storing data.

4. The fourth part is to send email using smtplib protocol, and attach the updated weather information to the title of the email. Additionally, attaching the csv file as well as html format in line with Fortuna official picture into the email content.

5. The fifth part is to define the condition of minimal temperature for external trigger via email

6. The sixth part is to schedule external trigger

####   Note: 
For security reason, the passwords of sender email and of the database are stored in the attached json files separately.
