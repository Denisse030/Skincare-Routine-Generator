# **Skincare Routine Generator (Skin 1004 Edition)**

## Project Overview

This program generates a personalized skincare routine using only Skin 1004 products.
After entering your **skin type** and **skin concerns**, the program curates a full morning (AM) and night (PM) routine.
It also includes product warnings, adds usage notes for facemasks and treatments, and gives the option to view key ingredients.

---
## Features:

* Generates tailored AM and PM skincare routines
* Matches products to skin types and concerns
* Displays product warnings and usage notes
* Allows users to view key ingredients for each product
* Interactive and user-friendly command-line interface
  
---
## Project Structure
```
Skincare-Routine-Generator/
│
├── classes.py         # Defines Product and SkinProfile classes
├── data_loader.py     # Loads product data from a JSON file
├── rules.py           # Contains logic for matching and routine generation
├── main.py            # Main program entry point (for user interaction)
├── test_classes.py    # Unit tests for verifying the apps functionality
├── __init__.py        # Marks the directory as a Python package, enabling module imports.
└── data/
    └── products.json  # Product dataset (Skin 1004 products)
```

---
## Technologies Used
* Python 3.10+
* Typing module (`List`, `Set`, `Optional`, etc.)
* JSON (for structured data loading)
* Command-line input and output

---
## How to Run the Program

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Skincare-Routine-Generator.git
    cd Skincare-Routine-Generator
    ```
2. **Ensure Python 3.10 or higher is installed:**
   ```bash
   python --version
   ```
3. **Run the main program:**
   ```bash
   python main.py
   ```
5. **Follow the on-screen prompts:**
   * Enter your skin type (dry, oily, combination, or sensitive)
   * Enter your skin concerns (e.g., acne, calming, hydrating, etc...)
   * View your custom routine, warnings, and key ingredients

---
## Running Tests

You can verify that the main classes and functions work correctly by running:
```bash
python test_classes.py
```

---
## Documentation Standards

Each file and function in this project includes clear docstrings following **PEP 257** guidelines.
Every class, method, and function (except standard dunder methods) contains a description of its purpose, parameters, and return values.
This ensures code readability and proper documentation for maintainability and grading.

---
## Author

**Denisse Benito Gutierrez**

- Boston University MET College — MS in Software Development
- Course: CS521 — Fall 2025
- Professor Eugene Pinsky

---
## Future Improvements

* **Convert to a Web Application:**
  Transform the command-line program into a modern **web application** using **React** for the front end.
  This would allow users to access their personalized routines through a clean, interactive interface.

* **Expand Product Database:**
  Include **multiple skincare brands and product lines** instead of only Skin 1004, allowing for broader recommendations and customization.

* **Add More Skin Concerns:**
  Extend the list of recognized skin concerns (e.g., redness, texture, sensitivity, aging) to make results more accurate and inclusive.

* **Increase Personalization:**
  Use more detailed user input such as age, climate, and routine preferences to tailor product recommendations even further.

* **Custom Routine Steps:**
  Allow users to choose how many **steps** they want in each routine (for example, minimal, standard, or extended) to match different lifestyles and preferences.


