# Voice-Controlled Smart Home (Arabic & English) – Graduation Project

With the rapid development of smart technologies, smart homes have become an essential part of modern life. Voice-based interaction offers a natural and hands-free way to control home devices, improving both comfort and accessibility.
This graduation project presents a Voice Controlled Smart Home System that allows users to monitor and control home appliances through a mobile application and voice commands, integrated with IoT hardware.

# Project Objective

The main objectives of this project are:

To design a smart home system controlled using voice commands

To provide a mobile application for monitoring and controlling devices

To enable secure access through user authentication

To integrate speech processing with IoT hardware

To build a scalable system that supports future enhancements

# System Overview

The system consists of three main components:

1- Mobile Application (Flutter)

2- Voice Processing & Control Logic (Python)

3- IoT Hardware Layer (ESP-based controller)

The user interacts with the system through the mobile application, which displays the current state of all connected devices and allows voice-based control.

# Mobile Application

The mobile application is responsible for user interaction and system control.

### Features:

User Authentication

Login using email and password

### Device Dashboard

Displays all connected devices

Shows the current status of each device (ON / OFF)

### Voice Control

Allows the user to record voice commands

Sends commands to the control system for processing

The application is designed with a simple and user-friendly interface to ensure ease of use.

# Voice Control System

The voice control module handles speech input and command understanding.

### Workflow:

1- The user records a voice command

2- The audio is processed and converted to text

3- The command text is analyzed to extract:

Action (e.g., turn on, turn off)

Device (e.g., light, fan)

Location (e.g., kitchen, room)

4- The extracted command is converted into a structured format

5- The command is sent to the IoT controller for execution

The system is designed to support both English and Arabic voice commands, making it more flexible and user-friendly.

# IoT Hardware Layer

The hardware layer is responsible for executing the commands received from the control system.

## Components:

ESP-based microcontroller (ESP32 / ESP8266)

Relays connected to home appliances

Devices such as lights and fans

## Functionality:

Receives control commands from the application

Turns devices ON or OFF accordingly

Updates the device status to reflect the current state

The hardware is programmed using C++ and follows a modular design to allow easy expansion.

# Technologies Used
## Software:

Flutter – Mobile application development

Python – Voice processing and command handling

Speech-to-Text & NLP libraries

C++ / Arduino Framework – ESP programming

## Hardware:

ESP-based microcontroller

Relays and connected smart devices

# System Advantages

Hands-free smart home control

Simple and intuitive user interface

Secure user authentication

Real-time device status monitoring

Scalable design for adding more devices

# Future Work

The system is designed to support future enhancements, including:

Integration of smart cameras for home monitoring

Implementing voice biometric authentication (voice fingerprint) for secure access

Adding more smart home devices

Expanding automation scenarios and smart modes
