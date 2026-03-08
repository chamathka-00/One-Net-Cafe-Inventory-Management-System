# One Net Cafe — Inventory Management System

A Python-based command-line application for managing inventory and suppliers at an internet café. The system handles item tracking, dealer selection, file storage, custom sorting, and menu-driven interactions — built entirely with functional decomposition, custom algorithms, and no external libraries.



## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies and Concepts](#technologies-and-concepts)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage Guide](#usage-guide)
- [File Handling](#file-handling)
- [License](#license)



## Overview

One Net Cafe simulates a real inventory management workflow for an internet café. Users can add, update, delete, and view stock items, save records to file, randomly select dealers from a loaded dataset, and inspect dealer inventory. All sorting is implemented using custom algorithms — no built-in `sort()` calls are used anywhere in the codebase.



## Features

### AID — Add Item Details
- Prompts for: Item Code, Name, Brand, Price, Quantity, Category, and Purchased Date
- Validates all inputs and checks for duplicate item codes before saving

### DID — Delete Item Details
- Deletes an existing item by item code
- Includes validation to handle non-existent codes gracefully

### UID — Update Item Details
- Updates any field of an existing item using its item code
- Only the selected field is changed; all other data is preserved

### VID — View Items Table
- Displays all items in a clean, formatted table
- Sorted in descending order by item code using a custom sorting algorithm
- Shows the current total value of all purchased items

### SID — Save Item Details
- Saves all current item data to a text file
- Handles file validation, overwrite confirmation, and consistent formatting

### SDD — Select Four Random Dealers
- Loads dealer records from a text file
- Randomly selects 4 unique dealers with no duplicates
- Each dealer entry contains: Name, Contact Number, Location, and 3 items (Name, Brand, Price, Quantity)

### VRL — View Randomly Selected Dealers
- Displays full details of all randomly selected dealers
- Sorted by Location using a custom sorting algorithm

### LDI — List Items of a Given Dealer
- Displays the inventory of one specific dealer based on user input

### ESC — Exit
- Clean program shutdown with a confirmation message



## Technologies and Concepts

| Concept | Usage |
|---|---|
| Python 3 | Primary language |
| Functions and modular design | All features are decomposed into reusable functions |
| Loops (`for`, `while`) | Iteration over records, menus, and validation |
| Conditionals | Input validation, duplicate checks, branching logic |
| Exception handling | Safe handling of invalid inputs and file errors |
| Custom sorting algorithms | Descending sort by item code; sort by dealer location |
| File handling | Read dealer data; write and overwrite item records |
| Lists and dictionaries | Core data storage for items and dealers |
| Console-based UI | Menu-driven interface with full input validation |



## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd one-net-cafe
   ```

2. Ensure the dealer data file is present in the project directory (required for the SDD and VRL features).

### Running the Application

```bash
python main.py
```

The system launches a numbered menu. Enter the corresponding command code to select any operation.



## Usage Guide

| Command | Operation |
|---|---|
| AID | Add a new item to inventory |
| DID | Delete an item by item code |
| UID | Update fields of an existing item |
| VID | View all items in a sorted formatted table |
| SID | Save all item data to a text file |
| SDD | Randomly select 4 dealers from file |
| VRL | View selected dealers sorted by location |
| LDI | List items belonging to a specific dealer |
| ESC | Exit the application |



## File Handling

- **Dealer data** is loaded from a pre-existing text file at runtime. The file must be present in the project directory for dealer-related features to function.
- **Item data** is saved to a text file using the SID command. The system prompts before overwriting an existing file and writes all records in a consistent, readable format.


## License

This project is licensed under the [MIT License](LICENSE).
