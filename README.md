# EE-374-FUNDAMENTALS-OF-POWER-SYSTEMS-AND-ELECTRICAL-EQUIPMENT-2022-2023-SPRING-TERM-PROJECT

In this project you will be given a random transmission tower’s specifications in a text file. Also, you
will be provided with a library of ACSR conductors. In Phase 1, you are supposed to find a tool to
preprocess the raw input data given in text format into a useful format for Phase 2 applications. In other
words, you will create a function file that reads formatted data from text in PYTHON environment. In
Phase 2, depending on these data your code should calculate the resistance (R), reactance (X) and
susceptance (B) of the overhead line in per unit quantities.
These information will be valid for the transmission line to be modeled:
• You will be given only 3-phase systems (no single-phase systems)
• All phases consist of the same bundle orientation and same type of conductors
• Lines are transposed. The transposition rule is as follows.
Transposition
cycle section  Position 1  Position 2  Position 3
1                 Phase A   Phase B       Phase C
2                 Phase C   Phase A       Phase B
3                 Phase B   Phase C       Phase A
