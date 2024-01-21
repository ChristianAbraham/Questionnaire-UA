# Universitas Airlangga Questionnaire AutoFill

## Overview

This project is a Behave-Selenium automation script designed to automatically fill in the Universitas Airlangga questionnaire. It simulates the user journey through the website, providing predefined inputs to ease the process.

## Prerequisites

Before using this automation script, ensure you have the following prerequisites installed:

- Python 3.x: https://www.python.org/downloads/
- Behave: Install using `pip install behave`
- Selenium: Install using `pip install selenium`
- ChromeDriver: Download the appropriate version from https://sites.google.com/chromium.org/driver/ and ensure it's in your system's PATH.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/unair-questionnaire-autofill.git
   cd unair-questionnaire-autofill
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute the Behave test:

   ```bash
   behave
   ```

   This will launch a Chrome browser, navigate through the Universitas Airlangga website, and automatically fill in the questionnaire based on the predefined steps in the feature file.

## Important Note

- Make sure to replace `"username"` and `"password"` in the `when` steps with your actual Universitas Airlangga login credentials.
- Keep the ChromeDriver up to date with your Chrome browser version.

## Disclaimer

This script is for educational and personal use only. Use it responsibly and in accordance with the terms of service of the Universitas Airlangga website.

---
