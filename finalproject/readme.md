# This is my **BUS443 Final Project**

Project Includes:
- **Login screen:** The first screen/view should be a login/authentication screen.
You should not be able to access any other screen within the app unless the user is
authenticated. So all unauthenticated users should be redirected to the login page.

- **Base HTML:** The base HTML should have all the navigation links. Think Navbar or
Sidebar. This should be common for all individual HTML pages you will be
developing. Django allows you to do this by “extendingbase.html”

- **Dashboard – Home/Main screen:** The main screen/view after login should be a
dashboard. The dashboard should contain information about number of enrolled
students, average GPA, number of seniors, juniors and freshmen etc. Try to be
innovative with your dashboard designs. Use of charts to highlight this information is
preferred/encouraged. The information should be retrieved from the database. Please
do not hard code the numeric values in the html files.

- **Student details:** This screen will be an info screen that displays student information (first
name, last name, major, year and GPA). You can use a table to display this info. Use
pagination to limit a single view to show only 10 students at a time. Since there are 20
students, this information would be displayed in two pages.

- **Book details:** This an info screen that shows all the books in the database. You can
use a table to display this information. The data should be sorted from highest to lowest
by “Number of times previously checked out”.Paginate this information so that data is displayed in two pages.

- **Book reservation:** This screen should allow a user to reserve a book for the student. The
screen can have two dropdown boxes. One dropdown box that shows student names
and the other that shows book names. When a student and book name is selected, on
click of the “Reserve” button, the book should be reserved for thatstudent. The book
reservation should be successful only if these below criteria are satisfied. Use ajax to
send the data to the backend. 