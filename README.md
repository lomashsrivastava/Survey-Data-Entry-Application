Office Attendance System

Description

This Office Attendance System is a desktop application built using Python and Tkinter for managing employee attendance with live face capture. The system allows users to mark attendance by entering their Employee ID and Name, while simultaneously capturing their live image using a webcam.

Features

Employee ID and Name Input

Automatic Time & Date Recording

Live Camera Preview

Image Capture with Attendance

Real-time Attendance Record Display

Scrollable Attendance Records

Animated Success Effect

Modern UI with Color Themes

Technologies Used

Python

Tkinter (GUI Development)

OpenCV (Image Capture)

JSON (Data Storage)

Pillow (Image Processing)

Installation

Clone the repository:

git clone https://github.com/yourusername/attendance-system.git cd attendance-system

Install the required libraries:

pip install opencv-python-headless Pillow

Run the Application:

python a.py

Folder Structure

attendance-system/ ├─ attendance_data.json # Attendance data file ├─ attendance_images/ # Captured employee images └─ a.py # Main Application File

How to Use

Enter the Employee ID and Name in the input fields.

The live camera feed will display your image.

Click on Mark Attendance.

The system will capture your image and store it with the timestamp.

The attendance record with the captured image will be displayed.

Preview

License

This project is licensed under the MIT License.

Author

Lomash Srivastava

Contributing

Feel free to raise issues or submit pull requests!


Indian Railway Reservation System
Overview
The Indian Railway Reservation System is a GUI-based application built using Python and Tkinter. It allows users to register, log in, book train tickets, generate barcodes for payments, and check PNR statuses. The system provides a user-friendly interface with modern themes using the ttkbootstrap library.

Features
User Registration and Login System
Ticket Booking with Passenger Details
Journey Class Selection
Payment Gateway Simulation (UPI & Barcode Generation)
QR Code Barcode Generation for Payments
PNR Status Check
Dynamic Theme Switching
Ticket Storage with PNR Mapping
Modern GUI Design
Technologies Used
Python
Tkinter
ttkbootstrap (Themed Widgets)
Pillow (Image Processing)
qrcode (QR Code Generation)
Random Library
Time Library
Installation
Clone the repository:

git clone https://github.com/username/railway-reservation-system.git
cd railway-reservation-system
Install the required dependencies:

pip install pillow qrcode ttkbootstrap
Run the application:

python railway_reservation.py
How to Use
Registration
Launch the application.
Click on Register / Login.
Enter your personal details like Full Name, Mobile Number, Aadhaar Number, Age, Address, Pincode, User ID, and Password.
Click on Submit to register.
Login
Go to the Login Screen.
Enter your User ID and Password.
Click Login to proceed to the ticket booking section.
Ticket Booking
Enter passenger details including Name, Age, Train Name, Train Number, Departure, and Destination Stations.
Select the Journey Class from the dropdown.
Choose the Journey Date.
Click Proceed to Payment.
Payment
Choose either UPI Payment or Generate Barcode.
For Barcode Payment, scan the generated QR code.
Payment will be confirmed automatically after 30 seconds.
PNR Status
Go to the PNR Status Check screen.
Enter your PNR number.
Click Check Status to view your booking details.
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
📂 railway-reservation-system
├─ railway_reservation.py  # Main Application File
├─ barcode.png            # QR Code Image
└─ README.md             # Project Documentation
Dependencies
Python 3.x
Pillow
qrcode
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
Indian Railway Official Website (Design Reference)


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



