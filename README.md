# REST-API
REST-API

## Main takeaway
### Part 1
* What is a **REST API**?
  * An API, or application programming interface, is a set of rules that define how applications or devices can connect to and communicate with each other. A REST API is an API that conforms to the design principles of the REST, or representational state transfer architectural style. For this reason, REST APIs are sometimes referred to RESTful APIs.
* This repo is a **Flask project** with **REST API endpoints**
  * **Flask** is a web framework, it’s a Python module that lets you develop web applications easily
* My **API endpoints** are located at http://localhost:8000/api + the endpoint specific path
  * The host and port are defined in `app.run` in *app.py*
  * The endpoint specific paths are defined *swagger.yml* under paths
* [Swagger UI API documentation](https://github.com/swagger-api/swagger-ui)
  * *Swagger UI is a collection of HTML, JavaScript, and CSS assets that dynamically generate beautiful documentation from a Swagger-compliant API.*
* The **OpenAPI Specification** is an API description format for REST APIs and provides a lot of functionality, including:
  * Validation of input and output data to and from your API 
  * Configuration of the API URL endpoints and the expected parameters
* The **OpenAPI Specification**, previously known as the Swagger Specification, is a specification for a machine-readable interface definition language for describing, producing, consuming and visualizing RESTful web services
* When you use OpenAPI with Swagger, you can create a user interface (UI) to explore the API
  * An **API documentation** is created at http://localhost:8000/api/ui
* The **Connexion module** allows a Python program to use the OpenAPI specification with Swagger.
* *swagger.yml* is the **API Configuration File**

### Part 2
* Serializer = To convert complex data types to and from Python data types, you’ll need a serializer. For this tutorial, you’ll use [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/).
* **SQLAlchemy** will sanitize user data (Little Bobby tables) for you before creating SQL statements. It’s another big advantage and a reason to use SQLAlchemy when working with databases.
  * SQLAlchemy is a big project and provides a lot of functionality to work with databases using Python. One of the features that it provides is an object-relational mapper (ORM). This ORM enables you to interact with the person database table in a more Pythonic way by mapping a row of fields from the database table to a Python object.
* **SQL** = structured query language
  * Unlike programming languages like Python, SQL doesn’t define how to get the data. SQL describes what data is desired and leaves the how up to the database engine.
  * SQLite is a widely used **relational database management system (RDBMS)** that doesn’t need a SQL server to work