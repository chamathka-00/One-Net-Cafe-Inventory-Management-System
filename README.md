# One Net Cafe – Inventory Management System

CM1601 – Programming Fundamentals

BSc (Hons) Artificial Intelligence & Data Science

Robert Gordon University (RGU)

Coursework 1 – Y1S1

## 📌 Project Overview

One Net Cafe is a Python-based command-line application developed for the CM1601 Programming Fundamentals module.
It is built around the real-world scenario of David, who is opening an internet café and requires a system to manage inventory and suppliers. The program simulates item tracking, dealer selection, file handling, sorting, and menu-driven interactions—core skills required in the module.

This system is fully aligned with the coursework requirements, including custom sorting algorithms, input validation, text-file storage, and functional decomposition.

## 🎯 Learning Objectives

This project demonstrates the ability to:

* Apply algorithmic problem-solving

* Design, code, compile, test, and run programs using Python

* Build robust, maintainable code using functions

* Implement loops, conditionals, collections, file handling, and custom sorting algorithms

* Use exception handling and input validation effectively

* Construct a clean, interactive console menu system

## 🖥️ System Features
🔹 **AID – Add Item Details**

Prompts the user for:
Item Code, Name, Brand, Price, Quantity, Category, Purchased Date
Includes validation and duplicate record checks.

🔹 **DID – Delete Item Details**

Deletes an item by item code with proper validation.

🔹 **UID – Update Item Details**

Updates any of the fields of an existing item using the item code.

🔹 **VID – View Items Table**

* Displays all items in a neat formatted table

* Sorted using a custom sorting algorithm (descending by item code)

* Displays current total value of purchased items

🔹 **SID – Save Item Details**

Saves all item data to a text file at any time.
Implements file validation, overwrite handling, and consistent formatting.

🔹 **SDD – Select Four Random Dealers**

* Loads dealer data from text file

* Randomly selects 4 dealers

* Ensures no duplicates

* Displays: “4 Dealers are Selected Randomly”

Each dealer contains:
Name, Contact No, Location, 3 items (Name, Brand, Price, Quantity)

🔹 **VRL – View Randomly Selected Dealers**

Displays all details of selected dealers, sorted by Location using a custom sorting algorithm.

🔹 **LDI – List Items of a Given Dealer**

Displays the items of one selected dealer based on the user’s input.

🔹 **ESC – Exit**

Clean program shutdown.

## 📂 Project Structure
OneNetCafe/

&nbsp;&nbsp;&nbsp;│── main.py

&nbsp;&nbsp;&nbsp;│── dealers.txt

&nbsp;&nbsp;&nbsp;│── items.txt

&nbsp;&nbsp;&nbsp;│── README.md

## ⚙️ Technologies & Concepts Used

* Python 3

* Functions and modular design

* Loops (for, while)

* Conditionals

* Exception handling

* Custom sorting algorithms (not built-in sort)

* File handling (read/write)

* Collections (lists, dictionaries)

* Console-based UI with validation

## 🚀 How to Run

1. Install Python 3

2. Ensure dealers.txt and items.txt are in the same directory

3. Run the script:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python main.py

## 📜 Academic Integrity

This repository contains original code written for submission to RGU.
Reusing or submitting this work elsewhere without attribution may violate academic integrity guidelines.

## 📘 License

This project is licensed under the Apache License 2.0.
You may view, use, and adapt the code for learning and educational purposes, provided that proper attribution is given as required by the license.

Submitting this work, or any modified version of it, as part of an academic assessment is strictly prohibited.
