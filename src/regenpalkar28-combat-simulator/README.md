# ⚔️ Combat Simulator 🎲  
A turn-based battle simulator built with **Pygame**, featuring animated combat, dice-based attacks, and dynamic health systems. Players and AI-controlled enemies take turns rolling dice to determine their attack power, bringing an element of randomness and strategy to each round.

---

## 💡 How It Works
- **Player vs. Bot Combat:** The player (Knight) and bot (Ninja) each start with a set amount of health, attack power, and defense.  
- **Dice Roll Mechanic:** Before every attack, a dice roll determines the multiplier for the attack power.  
- **Attack Animation:** The attacker moves toward the opponent during their turn to visually represent the strike.  
- **Damage Calculation:**  
  `damage = (attack_power × (dice_number + 1)) − defense`  
  If damage is negative, it’s set to zero.  

- **Health Bars & Damage Display:** Each character has a visual health bar, and floating text briefly shows the damage dealt.  
- **Game Flow:**  
  - Player clicks **"Roll Dice"** to start their attack.  
  - After the attack animation, the bot rolls automatically.  
  - The game continues until one character’s health reaches zero.  
  - A victory message appears for the winner.

---

## 🕹️ Controls
- **Mouse Click** on the “Roll Dice” button to perform your turn.  
- The rest of the game proceeds automatically.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have **Python 3.x** installed, along with **Pygame**:

```bash
pip install -r requirements.txt
```

### How to run?
- To open this combat simulator, simply type these commands in the command line

```bash
cd regenpalkar28-combat-simulator
Combat.py
```