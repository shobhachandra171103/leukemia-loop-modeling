# Protein Structural Modeling for Leukemia Research

This project uses the biological homology tool **MODELLER** to clean up and predict loops in target protein structures.

## What I accomplished:
* Set up a working Linux terminal environment for bioinformatics tools.
* Fixed package dependencies to install the official Sali Lab MODELLER suite.
* Configured academic licensing and successfully executed automated Python scripts (`getseq.py`, `predict.py`) to align sequence fragments and compute 3D atomic coordinates.

## Model Visualization
Below is the structural overlay of the generated candidate models:

![Structural Overlay of Loop Models](leukemia-model.png)

## Biological Interpretation of the Image:
* **Conserved Core:** The highly structured alpha-helices (spirals at the bottom) align tightly across all models, showing structural stability.
* **Loop Flexibility:** The disorganized, wavy strands at the top represent the flexible loop regions. The engine generated multiple structural coordinates to sample how this loop bends and moves in a biological environment.
