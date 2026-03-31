# Digital Logic Simulator with WaveDrom Output

This project implements a lightweight combinational logic simulator in Python that parses a custom netlist format, evaluates logic circuits, and generates waveform outputs in WaveDrom-compatible JSON format.

## Features
- Parses structured netlist files (INPUTS, OUTPUTS, GATES, STIMULUS)
- Supports basic logic gates: AND, OR, XOR, NOT
- Simulates circuit behavior over time using input stimulus
- Generates waveform outputs for visualization using WaveDrom
- Command-line interface using argparse

## File
- `digitalsim.py` → main simulator implementation

## Input Format

The simulator expects a `.net` file with the following sections:
