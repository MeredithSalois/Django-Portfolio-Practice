# Django Portfolio Practice
```html
<h1>Django ToDo/Portfolio App</h1>

<p>This project encompasses the development of a Django application within the mysite project hosted on PythonAnywhere. The task involves creating either a ToDo app or a Portfolio app, departing from the traditional "blog" app. The starting point is Assignment 4, where the basic functionalities of adding and displaying ToDo items or portfolio items are established. Subsequently, the application evolves to incorporate advanced features such as forms and user logins.</p>

<h2>Implementation Overview:</h2>

<ul>
  <li><b>HomeView (LoginRequiredMixin, View):</b>
    <ul>
      <li>Renders the main page of the application.</li>
      <li>Retrieves all projects from the database and passes them to the template.</li>
    </ul>
  </li>
  <li><b>ProjectCreateView (View):</b>
    <ul>
      <li>Renders the form for creating a new project.</li>
      <li>Handles the POST request to save a new project to the database.</li>
    </ul>
  </li>
  <li><b>ProjectDetailView (View):</b>
    <ul>
      <li>Renders the detailed view of a specific project.</li>
      <li>Retrieves the project object based on the provided project ID.</li>
    </ul>
  </li>
  <li><b>ProjectEditView (View):</b>
    <ul>
      <li>Renders the form for editing an existing project.</li>
      <li>Handles the POST request to update the project details.</li>
    </ul>
  </li>
  <li><b>ProjectDeleteView (View):</b>
    <ul>
      <li>Renders the confirmation page for deleting a project.</li>
      <li>Handles the POST request to delete the specified project.</li>
    </ul>
  </li>
</ul>

<h2>Instructions:</h2>

<p>To run this application, ensure you have Django installed in your Python environment. Clone this repository and navigate to the project directory. Run the Django development server using the command <code>python manage.py runserver</code>. Access the application through the provided URL.</p>

<h2>Screenshots:</h2>

<p>Include screenshots of the running Django web application to showcase its functionality and user interface.</p>

<p>This project serves as a comprehensive example of building a Django application, demonstrating fundamental CRUD (Create, Read, Update, Delete) operations and integrating user authentication for enhanced security and functionality.</p>
