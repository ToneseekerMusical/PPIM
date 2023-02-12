# PPIM
Python Payload Instance Manager

Python Payload Instance Manager is a tool built for windows that aims to reduce the complexity of setting up a local PayloadCMS instance for development and making the CMS more accessible to those who have little to no experience coding. The project is currently in its infancy and isn't even fully functional at the moment, but I'd like to put this out for the community to leave feedback as the project develops, improve my coding knowledge, and contribute to the PayloadCMS project by lowering the learning curve for Wordpress users.

At this point in time, the GUI is under construction. Currently, the program will download MongoDB, MongoSH, MongoDB Compass, NodeJS, Github CLI, and VSCode during the setup, add the paths to your system's PATH environment variable, install MongoDB as a service, create the application's database, write the dependency information to the database and allow you to start and stop MongoDB, and open MongoSH and Compass from the interface. The next step is to create a database using the information provided in the startup screen, add the site info to the application database, and automate the install of a PayloadCMS website on your local machine. After that has been implemented, site management tools will be added, as well as automatic update detection, and application settings.

![image](https://user-images.githubusercontent.com/105748910/218302565-936208a6-8f3e-4289-b1b9-f30082698a68.png)
On starting up the program you will be met with the add project screen where you can designate various project information, your github repository for the project, database information, select plugins to install with the new project, and a command line interface that displays a readout of what is currently being executed on your computer.

The sidebar contains database controls to start and stop the MongoDB database, and display its current state, buttons to update the node and MongoDB versions installed with the program, as well as a settings tab to modify various settings such as default user name and password, your github credentials, MongoDB connection details etc

PPIM is built using customtkinter and tkinter at this moment, these dependencies are guaranteed to change without notice, so please, be sure to ensure you have the required packages in the requirements.txt installed.
