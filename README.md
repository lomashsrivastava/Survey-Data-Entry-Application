Survey Data Entry Application
Overview
The Survey Data Entry Application is a GUI-based system built using Python and Tkinter. It allows users to register, log in, create and manage surveys, collect responses, and generate reports. The system provides an intuitive user interface with modern themes using the ttkbootstrap library.

Features
User Registration and Login System
Survey Creation and Editing
Dynamic Question Types (MCQs, Text Input, Dropdowns)
Data Entry and Validation
Response Collection and Storage
Export Survey Data to CSV
Graphical Report Generation
Modern GUI Design with Theme Switching
Technologies Used
Python
Tkinter
ttkbootstrap (Themed Widgets)
Pandas (Data Handling)
Matplotlib (Data Visualization)
CSV (Data Export)
Random Library
Time Library
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/username/survey-data-entry.git  
cd survey-data-entry  
Install the required dependencies:

bash
Copy
Edit
pip install pandas matplotlib ttkbootstrap  
Run the application:

bash
Copy
Edit
python survey_app.py  
How to Use
Registration
Launch the application.
Click on Register / Login.
Enter your details like Full Name, Email, Mobile Number, User ID, and Password.
Click Submit to create an account.
Login
Go to the Login Screen.
Enter your User ID and Password.
Click Login to access the survey dashboard.
Creating a Survey
Click on Create New Survey.
Enter Survey Title and Description.
Add questions (choose from MCQs, Text Input, or Dropdowns).
Click Save Survey to store it.
Collecting Responses
Select a survey from the list.
Click Start Survey and enter responses.
Responses are automatically saved in the database.
Exporting Survey Data
Open the Survey Reports section.
Select the survey you want to export.
Click Export to CSV to download responses.
Generating Reports
Go to the Analytics Dashboard.
Select a survey and view graphical reports (Bar Charts, Pie Charts).
Data visualization is powered by Matplotlib.
Themes Available
Cosmo
Flatly
Journal
Lumen
Minty
Pulse
Sandstone
Yeti
Folder Structure
plaintext
Copy
Edit
📂 survey-data-entry  
├─ survey_app.py         # Main Application File  
├─ responses.csv         # Stored Survey Responses  
└─ README.md             # Project Documentation  
Dependencies
Python 3.x
Pandas
Matplotlib
ttkbootstrap
License
This project is licensed under the MIT License.

Author
Lomash Srivastava

Contact
Email: lomashgroups@gmail.com
GitHub: Lomash Srivastava
Acknowledgements
Tkinter Documentation
ttkbootstrap Library
Survey Form Design References
This version aligns perfectly with the Survey Data Entry Application while maintaining clarity, structure, and professionalism. 🚀 Let me know if you'd like any refinements!
