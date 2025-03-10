# RISC-V Assembler & Simulator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

A robust command-line tool built in Python that assembles RISC-V assembly code into machine code and simulates its execution. Perfect for learning and debugging RISC-V programs.

---

## Overview

This project implements a three-pass assembler and simulator for a subset of the RISC-V 32-bit integer ISA. The assembler verifies the syntax of input assembly code and then converts it into plain-text machine code. The simulator takes this machine code as input and displays changes in the contents of each register after executing every instruction. It also reflects the final state of the data memory.

Developed using procedural programming and managed with Git, this tool is designed for both learning and debugging RISC-V assembly programs. Its capabilities include handling register operations, data memory loading/storing, conditional statements, and function calls.

---

## Features

- **Three-Pass Assembler:**  
  Verifies syntax, processes assembly instructions, and outputs plain-text machine code.
- **Simulation Engine:**  
  Executes the assembled machine code, showing register updates after each instruction and the final data memory state.
- **Command-Line Interface:**  
  Simple, text-based interaction to assemble and simulate code from input files.
- **Core Capabilities:**  
  - Register operations  
  - Data memory loading/storing  
  - Conditional statements  
  - Function calls
- **Procedural Programming Approach:**  
  Straightforward and modular design for easy understanding and extension.

---
