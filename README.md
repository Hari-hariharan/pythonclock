# pythonclock

## Introduction

> Tkinter GUI project for timekeeping

A simple clock GUI project that I worked on to improve coding habits,improve my knowledge of tkinter and plyer modules, and utilize a database. When complete, this will be a fully functioning program similar to the "Clock" app on Android . It has support for a local digital clock, remainder, alarms, and a timer at the moment. I had add customizable messages, sounds.

## Code Samples

 from plyer import notification
 
from tkinter import *

from tkinter.ttk import *

import datetime

import platform

import winsound

windows.mainloop()



## About the Python Project:

The objective of our project is to implement an clock using Python. Python consists of some libraries such as datetime and tkinter which help us to build the project using the current date and time as well as to provide a user interface to set the alarm,remainder and counter timer according to the requirement in 12 or 24-hour format.

#Prerequisites:

This project requires good knowledge of Python and GUI (Graphic User Interface). Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI.

#Project File Structure

First, let’s check the steps to build an Clock program in Python:

Importing all the libraries and modules required

calling all the functions which takes the argument of the time, the user wants to set the alarm on and automatically breaks when the time is up, with sound

Create a display window for user input.

#Modules Used:

Tkinter module belongs to a standard library of GUI in Python. It helps us to create a dialog box with any information that we want to provide or get from the users.

Datetime and time modules in python help us to work with the dates and time of the current day when the user is operating python and to manipulate it too.

Winsound module provides access to the basic sound playing machinery provided by Windows platforms. This is useful to generate the sound immediately when a function is called.

#Adding a Tkinter Tab Control

To add Tabs Control, We can Use Tkinter Notebook. Here we will add four tabs for Clock, Alarm, Remainder, Timer Each.


