# Tip Calculator Web App (Flask)

## Project Description
A simple and user-friendly **Tip Calculator** built with **Flask**.  
The app allows users to calculate the tip and total bill amount by entering:

- Bill Amount ($)
- Tip Percentage (%)

The calculator validates inputs to prevent errors, such as:

- Empty fields
- Non-numeric inputs
- Negative or zero bill amounts
- Tip percentage exceeding 100%
- Extremely high bill amounts

It displays **friendly error messages** if input is invalid.

---

## How to Run

### 1. Clone the repository
git clone <your-repo-url>
cd <repo-folder>

### 2. Create a virtual environment
python -m venv venv

### 3. Activate the virtual environment
macOS/Linux: source venv/bin/activate
Windows: venv\Scripts\activate

### 4. Install dependencies
pip install -r requirements.txt

### 5. Running the App
python app.py