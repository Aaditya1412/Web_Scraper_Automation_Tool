# 🧬 DNA Sequence Automation Tool

This project is a Python-based automation script that submits DNA sequences to the **SCFBio IIT-Delhi DNA Structure Prediction Server**, retrieves their predicted 3D structures (PDB files), and saves them locally.

## 🚀 Features

- Reads DNA sequences from a `.csv` file (one sequence per row)
- Automates browser interactions using **Selenium**
- Handles system-level pop-ups and downloads with **PyAutoGUI**
- Saves all resulting `.pdb` files in a local output directory
- Useful for batch-processing DNA sequences for structural analysis
  
## 🛠️ Technologies Used

- **Python 3.x**
- **Selenium** – Web browser automation
- **PyAutoGUI** – For handling OS-level file save dialogs
- **glob** – For file detection and renaming
- **pandas** – For reading the input CSV

## 🧑‍💻 How It Works

1. The script reads a CSV file containing DNA sequences.
2. It opens the SCFBio DNA Structure Prediction website.
3. For each sequence:
   - Inputs the sequence into the server
   - Submits the form
   - Waits for the structure to be generated
   - Automatically downloads the corresponding `.pdb` file
4. The file is saved in a local `output/` folder, named after the input sequence or row ID.

## 📝 Prerequisites

- Install Python 3
- Install the required packages:
  
```bash
pip install selenium pandas pyautogui

