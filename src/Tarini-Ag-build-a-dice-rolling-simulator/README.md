# Dice Rolling Simulator

A simple command-line dice rolling simulator built with Python. This interactive tool allows you to roll multiple dice with customizable sides and displays formatted results.

## Features

- Roll 1-10 dice at once
- Choose number of sides (2-20) for each die
- Interactive CLI interface
- Formatted output with emoji decorations
- Total sum calculation
- Input validation
- Graceful error handling

## Requirements

This project requires Python 3.6 or higher. No external dependencies are needed as it uses only the Python standard library.

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd src/Tarini-Ag-build-a-dice-rolling-simulator/
   ```

## Usage

Run the dice rolling simulator using Python:

```bash
python dice_rolling_simulator.py
```

### Example Session

```
🎲 Welcome to the Dice Rolling Simulator! 🎲

How many dice would you like to roll? (1-10): 3
How many sides should each die have? (2-20): 6

========================================
🎲 DICE ROLL RESULTS 🎲
========================================
Die 1: 4
Die 2: 2
Die 3: 6

Total: 12
========================================

Would you like to roll again? (yes/no):
```

## How It Works

The simulator:
1. Prompts you for the number of dice to roll (1-10)
2. Asks for the number of sides on each die (2-20)
3. Randomly generates results for each die
4. Displays individual results and total sum
5. Offers to roll again or exit

## Error Handling

- Invalid inputs (non-numeric values) are caught and prompt re-entry
- Out-of-range values trigger validation messages
- Keyboard interrupt (Ctrl+C) exits gracefully

## Contributing

This project is part of Hacktoberfest 2025. Feel free to fork, improve, and submit pull requests!

## License

This project is open source and available for educational purposes.

## Author

Created as part of the beginner-python-mini-projects-hacktoberfest-2025 repository.
