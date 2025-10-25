# 🎮 Color Block Puzzle Game

A Nokia-inspired falling block puzzle game with color-matching mechanics! Match 3 or more blocks of the same color to clear them and score points. Features combos, increasing difficulty, and addictive gameplay.

## 📸 Game Features

- **Classic Falling Block Gameplay** - Tetris-style pieces with color matching
- **Color Matching Mechanics** - Connect 4+ blocks of the same color to clear them
- **Combo System** - Chain reactions multiply your score!
- **Progressive Difficulty** - Speed increases as you level up
- **Multiple Block Shapes** - 9 different piece shapes
- **7 Vibrant Colors** - Easy to distinguish and match
- **Next Block Preview** - Plan your moves ahead
- **Smooth Controls** - Responsive keyboard controls

## 🚀 Installation & Running

1. **Install Pygame:**
   ```bash
   pip install pygame
   ```

2. **Run the game:**
   ```bash
   python block_puzzle_game.py
   ```

## 🎯 How to Play

### Objective
Match 4 or more blocks of the same color (horizontally or vertically connected) to clear them. The more you clear at once and the more combos you create, the higher your score!

### Controls

| Key | Action |
|-----|--------|
| **← / →** | Move block left/right |
| **↓** | Soft drop (move down faster) |
| **↑** or **Z** | Rotate clockwise |
| **X** | Rotate counterclockwise |
| **SPACE** | Hard drop (instant drop to bottom) |
| **P** | Pause/Unpause |
| **Q** / **ESC** | Quit game |
| **R** | Restart (when game over) |

### Gameplay Mechanics

1. **Falling Blocks**: Random colored block shapes fall from the top
2. **Placement**: Move and rotate blocks to position them
3. **Matching**: When a block lands, the game checks for color matches
4. **Clearing**: Groups of 4+ connected same-colored blocks disappear
5. **Gravity**: Remaining blocks fall down to fill gaps
6. **Combos**: If new matches form after gravity, you get combo bonuses!
7. **Scoring**: 
   - 10 points per block cleared
   - Combo multiplier: 1.5x for each combo level
   - Example: 2-combo = 1.5x, 3-combo = 2.25x, etc.

### Block Shapes

The game features 9 different block shapes:
- **I** - 4-block line
- **O** - 2x2 square
- **T** - T-shaped piece
- **L** / **J** - L-shaped pieces
- **S** / **Z** - Zigzag pieces
- **Line** - 2-block line
- **Dot** - Single block

### Difficulty Progression

- **Level Up**: Every 50 blocks cleared = +1 level
- **Speed Increase**: Each level makes blocks fall faster
- **Starting Speed**: 800ms per drop
- **Speed Decrease**: -50ms per level
- **Minimum Speed**: 100ms (at level 15+)

## 🎨 Color Palette

The game uses 7 bright, distinguishable colors:
- 🔴 **Red**
- 🟢 **Green**  
- 🔵 **Blue**
- 🟡 **Yellow**
- 🔵 **Cyan**
- 🟣 **Magenta**
- 🟠 **Orange**

## 📊 Scoring Strategy Tips

1. **Create Combos**: Try to set up cascading matches for huge score multipliers
2. **Plan Ahead**: Use the "Next" preview to plan your placement
3. **Build from Bottom**: Keep your stack low to avoid game over
4. **Color Grouping**: Try to group same colors together for easier matching
5. **Use Hard Drop**: Space bar is faster than waiting - use it strategically
6. **Clear Efficiently**: Larger matches give more points, but combos are king!

## 🏆 High Score Challenge

Can you reach:
- **1,000 points** - Beginner
- **5,000 points** - Intermediate  
- **10,000 points** - Advanced
- **25,000+ points** - Master!

## 🛠️ Technical Details

**Built with:**
- Python 3.x
- Pygame library

**Architecture:**
- Object-Oriented Design
- Flood-fill algorithm for color matching
- Gravity system with cascade detection
- Event-driven input handling
- 60 FPS smooth gameplay

**Grid Size:** 10 columns × 20 rows  
**Block Size:** 25×25 pixels  
**Screen Resolution:** 800×600 pixels

## 🎮 Game Over

The game ends when:
- A new block cannot be placed at the top of the board
- Blocks have stacked up to the very top row

When game over occurs, press **R** to restart or **Q** to quit.

## 🌟 Features Breakdown

### What Makes This Game Special

1. **Color Matching Instead of Lines**: Unlike traditional block games that clear full rows, this game rewards strategic color grouping
2. **Combo System**: Cascading matches create exciting chain reactions
3. **Flexible Strategy**: Multiple paths to success - go for big clears or consistent combos
4. **Progressive Challenge**: Speed increases naturally with skill level
5. **Visual Feedback**: Clear UI shows score, level, combos, and next piece

### Inspired By

- Classic Nokia puzzle games
- Panel de Pon / Tetris Attack mechanics
- Columns game series
- Modern match-4 puzzle games

---

**Ready to play? Run `python block_puzzle_game.py` and start matching! 🎮✨**
