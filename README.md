# 🪑 OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

---

## 🏢 Description

This project is based on the **BeCode challenge “Open Space Organizer”**.  
The goal of the challenge was to create a Python program that randomly assigns people to seats in an open space.  

The scenario:  
Our company moved to a new office at **CEVI Ghent**, an open space with **6 tables of 4 seats each (24 total)**.  
Since many colleagues are new, we came up with the idea of changing seats every day to get to know each other better by working side by side.  

The mission:  
Build a program that automatically re-assigns everyone to a new seat every day — randomly, fairly, and efficiently — while learning to use:
- **Object-Oriented Programming (OOP)**  
- **Clean imports and architecture**  
- **Functions and classes**  
- **Data from a .txt file**  
- **GitHub for version control**

This was my **first solo project** at BeCode.  
I worked on it for **two days**, tested a lot, and really enjoyed the learning process — especially seeing how everything fits together into a working application.

![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)

---

## 📦 Repository Structure

```
.
├── utils/
│ ├── table.py # Seat + Table classes
│ ├── openspace.py # OpenSpace logic
│ └── file_utils.py # Load names from .txt
├── main.py # Entry point for the program
├── names.txt # Input list of colleagues
├── openspace.csv # Output file (auto generated)
└── README.md

```

---
## ⚙️ Features

- Reads names from a **.txt file** (one name per line)  
- Randomly assigns everyone to tables and seats  
- Handles **overflow** (too many people)  
- Displays the full room setup directly in the terminal  
- Optionally saves the seating plan to **openspace.csv**  
- Uses **Object-Oriented Programming (OOP)** principles  
- Includes **typed functions, docstrings, and clean imports**

---

## 🛎️ Usage

1️⃣ Clone the repository to your local machine:  
`git clone https://github.com/pierrickvanhoecke/challenge-openspace-classifier.git`  
`cd challenge-openspace-classifier`

2️⃣ Add your list of names to a file called **names.txt**, one name per line.  

3️⃣ Run the script from the terminal:  
`python3 main.py names.txt --seed 7 --save`

4️⃣ The program will:  
- Read your file  
- Randomly organize your colleagues  
- Display the result in the console  
- Save the new seating plan to **openspace.csv**

**Example output:**

Open Space — tables: 6, capacity: 24, seats left: 0  
-----------------------------------------------  
Table 1:  
  Seat 1: Aleksei  
  Seat 2: Amine  
  Seat 3: Anna  
  Seat 4: Astha  
…  
✅ Everyone has a seat.  
Saved seating in: openspace.csv  

---

## ⏱️ Timeline

This project was developed in **2 days** as part of the **BeCode AI & Data Bootcamp**.  
It was completed **solo**, with a strong focus on testing, debugging, and learning to build a full Python project from scratch.

---

## 📌 Personal Situation

This was my **first official BeCode project** and my first complete Python application using multiple modules and classes.  
It taught me how to:  
- Work with **clean architecture and imports**  
- Apply **Object-Oriented Programming** (*Seat*, *Table*, *OpenSpace*)  
- Use **GitHub** effectively for version control  
- Build, test, and debug efficiently in **VS Code** and **Jupyter**

---

## 👨‍💻 Author

**Pierrick Van Hoecke**  
AI & Data Science Student @ BeCode Ghent  
Connect with me on [LinkedIn](https://www.linkedin.com/in/pierrick-van-hoecke-60b305310/)
---

## 🧰 Built With

- [Python 3](https://www.python.org/)  
- Object-Oriented Programming (OOP)  
- VS Code + Jupyter Notebook  
- Formatted with [Black](https://pypi.org/project/black/)

---

## 🏁 Future Improvements

All future improvements — such as:  
- Dynamic room setup from a `config.json` file  
- Preventing single-person tables  
- Adding new colleagues dynamically through user input  

are being developed in a **separate Git branch** (`feature/future-improvements`)  
as part of the *nice-to-have* section of the BeCode challenge.

---

**© 2025 — First BeCode project by Pierrick Van Hoecke**