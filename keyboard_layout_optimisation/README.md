# Keyboard Layout Optimization using Simulated Annealing

This project optimizes keyboard layouts to minimize typing cost using a stochastic optimization technique (Simulated Annealing). The goal is to generate an efficient keyboard arrangement based on input text frequency and character transitions.

## Features
- Optimizes keyboard layout based on typing cost
- Uses simulated annealing for global optimization
- Supports custom input text files
- Generates visualizations for optimization progress
- Outputs final optimized layout and statistics

## Files
- `kbd_optim.py` → main optimization algorithm
- `cost_trace.png` → cost vs iteration graph
- `layout.png` → optimized keyboard layout visualization
- `final_results.json` → final layout and performance metrics

## How to Run

### Default run
```bash
python kbd_optim.py
