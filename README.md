# **Skincare Routine Generator (Skin 1004 Edition)**

## Project Overview

This program generates a personalized skincare routine using only Skin 1004 products.
After entering your **skin type** and **skin concerns**, the program curates a full morning (AM) and night (PM) routine.
It also includes product warnings, adds usage notes for facemasks and treatments, and gives the option to view key ingredients.

## Features
- Generates tailored AM and PM skincare routines
- Matches products to skin types and concerns
- Displays product warnings and usage notes
- Allows users to view key ingredients for each product
- Interactive and user-friendly command-line interface

## Project Structure
Skincare-Routine-Generator/
│
├── classes.py         # Defines Product and SkinProfile classes
├── data_loader.py     # Loads product data from a JSON file
├── rules.py           # Contains logic for matching and routine generation
├── main.py            # Main program entry point (for user interaction)
├── test_classes.py    # Unit tests for verifying the apps functionality
└── data/
    └── products.json  # Product dataset (Skin 1004 products)

## How to Run the Program

1. Clone the repository:
    git clone https://github.com/your-username/Skin1004-Routine-Generator.git
    cd Skin1004-Routine-Generator
2. Ensure Python 3.10 or higher is installed:
   python --version
3. Run the main program
   python main.py
4. Follow the on-screen prompts:
   - Enter your skin type (dry, oily, combination, or sensitive)
   - Enter your skin concerns (e.g., acne, calming, hydrating)
   - View your custom routine, warnings, and key ingredients



