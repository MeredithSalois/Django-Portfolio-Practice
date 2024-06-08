# 👨‍💻 Django Portfolio Practice
<h2>Description: </h2>
This project encompasses the development of a Django application within the mysite project hosted on PythonAnywhere. The task involves creating either a ToDo app or a Portfolio app, departing from the traditional "blog" app. The starting point is Assignment 4, where the basic functionalities of adding and displaying ToDo items or portfolio items are established. Subsequently, the application evolves to incorporate advanced features such as forms and user logins.

<h2> Implementation Overview: </h2>
- <b>The codebase comprises various views responsible for different aspects of the application:</b>

<h2> HomeView (LoginRequiredMixin, View): </h2>
- <b>Renders the main page of the application.</b>
- <b>Retrieves all projects from the database and passes them to the template.</b>

<h2> ProjectCreateView (View): </h2>
- <b>Renders the form for creating a new project.</b>
- <b>Handles the POST request to save a new project to the database.</b>

<h2> ProjectDetailView (View): </h2>
- <b>Renders the detailed view of a specific project.</b>
- <b>Retrieves the project object based on the provided project ID.</b>

<h2> ProjectEditView (View): </h2>
- <b>Renders the form for editing an existing project.</b>
- <b>Handles the POST request to update the project details.</b>

<h2> ProjectDeleteView (View): </h2>
- <b>Renders the confirmation page for deleting a project.</b>
- <b>Handles the POST request to delete the specified project.</b>

<h2> Instructions: </h2>
- <b>To run this application, ensure you have Django installed in your Python environment. Clone this repository and navigate to the project directory. Run the Django development server using the command python manage.py runserver. Access the application through the provided URL.</b>

<h2> Screenshots: </h2>
- <b>Included screenshots of the running Django web application to showcase its functionality and user interface.</b>

<h2>This project serves as a comprehensive example of building a Django application, demonstrating fundamental CRUD (Create, Read, Update, Delete) operations and integrating user authentication for enhanced security and functionality.</h2>
