Barber Booking Website – Final Project Proposal
Pedro Brito Wenceslau 
StudentID X00217596 Email: x00217596@mytudublin.ie
Github repository: https://github.com/wenceslaupedro/BarberShopProject

1. Project Overview
This project consists of developing a web-based booking system for a barbershop. The main objective is to simplify the process of scheduling appointments between barbers and clients through an easy-to-use online platform. The system will allow clients to select a barber and book available time slots, while barbers will be able to manage their daily schedule and see all upcoming appointments.

The website will begin with a login page that provides two options: one for barbers and one for clients. Depending on the option selected, the user will access a different interface with specific functionalities.

The goal of this system is to demonstrate the integration of front-end development, back-end programming, and database management to create a complete full-stack web application. The project will also show how cloud services can be used to store and manage data.

2. System Functionality
The platform will have two main types of users: Barbers and Clients. Each user type will have different features and access levels.

2.1 Client Interface
Clients will be able to use the platform to book appointments quickly and conveniently. After accessing the client section, the user will be able to:
•	View a list of available barbers;
•	Select a barber of their choice;
•	View available dates and time slots;
•	Book an appointment;
•	Receive confirmation that the booking has been completed.
The booking system will ensure that time slots cannot be double-booked. When a client selects a time that has already been reserved, the system will automatically prevent the booking and prompt the user to select another available time.

This feature ensures efficient scheduling and prevents conflicts between appointments.

2.2 Barber Interface
Barbers will have their own dashboard where they can manage their daily schedule. After logging in, the barber will be able to:
•	View their appointment agenda;
•	See the list of clients booked for a specific day;
•	Check appointment times and details;
•	Manage their schedule.

This interface will allow barbers to easily track their daily workload and prepare for upcoming clients. The agenda will display appointments organized by date and time, making it easy to visualize the daily schedule.

3. System Architecture and Technologies
The application will be developed using a full-stack architecture, separating the front-end, back-end, and database layers.

3.1 Front-End
The front-end is responsible for the user interface and interaction. It will be built using the following technologies:
•	HTML – for the structure of the web pages.
•	CSS – for styling and layout.
•	JavaScript – for interactive features such as booking 

The front-end will include the following main pages:
1.	Login/selection page (Barber or Client)
2.	Client booking page
3.	Barber dashboard (agenda view)

3.2 Back-End
The back-end will be developed using Python. It will handle the business logic of the application and communication between the front-end and the database.

The back-end will be responsible for:
•	Processing booking requests
•	Checking available appointment slots
•	Storing booking information
•	Retrieving schedule data for barbers
•	Managing user interactions with the system

3.3 Database
All application data will be stored in a MySQL database hosted on Microsoft Azure. Using a cloud-based database allows the system to be scalable and accessible from anywhere.

The database will store important information such as:
•	Barber details
•	Client bookings
•	Appointment dates and times

A possible database structure could include the following tables:

1.	Barbers Table
•	barber_id
•	barber_name
2.	Clients Table
•	client_id
•	client_name
3.	Appointments Table
•	appointment_id
•	barber_id
•	client_name
•	appointment_date
•	appointment_time

The appointments table will link barbers with clients and store the scheduled time.

4. Expected Outcome
By the end of the project, the system will provide a functional online barbershop booking platform where clients can easily book appointments and barbers can manage their schedule efficiently.

This project demonstrates several important skills in web development, including:
•	Front-end design and user interaction;
•	Back-end programming and server logic;
•	Database design and cloud integration;
•	Full-stack application development.

The final product will simulate a real-world booking system similar to those used by many service businesses today.

5. Future Improvements and Additional Features
Although the initial version of the project will focus on the core booking functionality, the system could be expanded in the future with additional features to improve the user experience and provide more business value for the barbershop.

One possible improvement would be to expand the client database by storing additional information such as the client’s address and date of birth (DOB). This data would allow the system to support more advanced features and personalized services.
For example, storing the date of birth would allow the barbershop to offer birthday promotions, such as discounts or special offers for clients during their birthday month. This type of feature can help increase customer loyalty and encourage repeat visits.

Another possible feature would be the implementation of a loyalty reward system. The system could track the number of haircuts a client has booked and automatically apply rewards after a certain number of visits. For instance, after 9 paid haircuts, the 10th haircut could be free. This would require storing the number of completed appointments for each client in the database and updating it after every booking.

Additional improvements could also include:
•	Email or SMS appointment reminders to reduce missed bookings;
•	Online payment integration to allow clients to pay when booking;
•	Barber availability management, allowing barbers to set working hours or days off;
•	Admin panel for the shop owner to manage barbers, services, and promotions.

These future features would transform the project from a simple booking system into a more complete barbershop management platform, demonstrating how the system could be expanded and improved over time.


