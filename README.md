# BOOKSTORE

> This project implements an online website which serves as a bookstore for reading and lending books developed using Django. The application allows users to rate, review, upload books, form communities and chat with other users to exchange books.

A detailed presentation of the project can be found as [report.pdf](src/presentation.pdf) and the user documentation is available at [documentation.pdf](src/user_documentation.pdf). It was made as the final project for CS 251 - **Software Systems Lab** course in Autumn 2017 at Indian Institute of Technology (IIT) Bombay, India.

## Software Requirements
```
 Web Design - HTML, CSS, Bootstrap and Javascript
 Backend - Django
 Documentation - Latex, Doxygen
 ```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. Install the package:

   Clone the github [repo](https://github.com/saiteja-talluri/Bookstore.git) using
```
git clone https://github.com/saiteja-talluri/Bookstore.git
```
2. Activate Virtual Environment:  Navigate to the folder containing the package. Run the following command to activate 
the virtual environment

```
source myvenv/bin/activate
```
3. Install dependencies: Navigate to the folder containing the package. Run the following command to install the 
dependencies required (this may require root priveleges):

```
pip3 install -r requirements.txt
```
   Alternatively, check the dependencies which are listed in requirements.txt and install them manually.

4. Running the servers: There are two servers which need to be run parallel in two terminals, one for the web and
other for the chat. Run the following commands one on each terminal.

```
python3 manage.py runserver
python3 manage.py run_chat_server
```

## Authors

* **Saiteja Talluri** - [saiteja-talluri](https://github.com/saiteja-talluri)
* Saiteja Nangunoori
* Sathvik Reddy


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

-  Thanks to this excellent [repo](https://github.com/Bearle/django-private-chat/tree/dev/example) implementing the chat feature.
-  Thanks to this amazing [blog](https://simpleisbetterthancomplex.com/tutorial/) for excellent tutorials on Django.
