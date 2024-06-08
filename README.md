# Django Portfolio Practice
This project encompasses the development of a Django application within the mysite project hosted on PythonAnywhere. The task involves creating either a ToDo app or a Portfolio app, departing from the traditional "blog" app. The starting point is Assignment 4, where the basic functionalities of adding and displaying ToDo items or portfolio items are established. Subsequently, the application evolves to incorporate advanced features such as forms and user logins.

Implementation Overview:
The codebase comprises various views responsible for different aspects of the application:

HomeView (LoginRequiredMixin, View):

Renders the main page of the application.
Retrieves all projects from the database and passes them to the template.
ProjectCreateView (View):

Renders the form for creating a new project.
Handles the POST request to save a new project to the database.
ProjectDetailView (View):

Renders the detailed view of a specific project.
Retrieves the project object based on the provided project ID.
ProjectEditView (View):

Renders the form for editing an existing project.
Handles the POST request to update the project details.
ProjectDeleteView (View):

Renders the confirmation page for deleting a project.
Handles the POST request to delete the specified project.
Instructions:
To run this application, ensure you have Django installed in your Python environment. Clone this repository and navigate to the project directory. Run the Django development server using the command python manage.py runserver. Access the application through the provided URL.

Screenshots:
Include screenshots of the running Django web application to showcase its functionality and user interface.

This project serves as a comprehensive example of building a Django application, demonstrating fundamental CRUD (Create, Read, Update, Delete) operations and integrating user authentication for enhanced security and functionality.
