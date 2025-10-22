from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    total_tip = total_amount = 0
    error_message = ""
    
    if request.method == "POST":
        bill_input = request.form.get("bill", "").strip()
        tip_input = request.form.get("tip", "").strip()
        
        try:
            bill = float(bill_input)
            tip_percent = float(tip_input)
            
            # Validate bill
            if bill <= 0:
                error_message = "Bill amount must be greater than 0."
            elif bill > 1_000_000:
                error_message = "Bill amount is too high (max $1,000,000)."
            # Validate tip
            elif tip_percent < 0:
                error_message = "Tip percentage cannot be negative."
            elif tip_percent > 100:
                error_message = "Tip percentage cannot exceed 100%."
            else:
                total_tip = bill * (tip_percent / 100)
                total_amount = bill + total_tip
                
        except ValueError:
            error_message = "Please enter valid numbers for bill and tip."

    return render_template(
        "index.html",
        total_tip=round(total_tip, 2),
        total_amount=round(total_amount, 2),
        error_message=error_message
    )

if __name__ == "__main__":
    app.run(debug=True)
