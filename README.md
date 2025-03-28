# Extracellular Matrix Stiffness and Nutrient Availability Study

## Project Overview
This project visualizes experimental data comparing the growth patterns of double metastasis and HeLa cells under varying conditions of extracellular matrix stiffness and nutrient availability.

## Data Analysis Components
The project includes several Python scripts for analyzing different aspects of the cell growth data:

- `Absb_Grp1.py`: Analyzes absorbance data for Group 1
- `FBS_Grp2.py`: Processes FBS (Fetal Bovine Serum) data for Group 2
- `FBS_doubling_Grp2.py`: Calculates and visualizes cell doubling times for Group 2
- `FBS_Grp3.py`: Processes FBS data for Group 3

## Setup Instructions
1. Ensure Python 3.x is installed on your system
2. Install required packages:
   ```bash
   pip install matplotlib numpy pandas
   ```

## Running the Analysis
All scripts can be executed using the `run_all_scripts.bat` batch file:
```bash
./run_all_scripts.bat
```

Alternatively, run individual scripts directly:
```bash
python Absb_Grp1.py
python FBS_Grp2.py
python FBS_doubling_Grp2.py
python FBS_Grp3.py
```

## Project Structure
```
Data_Vis/
├── Absb_Grp1.py         # Absorbance analysis script
├── FBS_Grp2.py          # FBS analysis script for Group 2
├── FBS_doubling_Grp2.py # Cell doubling time analysis
├── FBS_Grp3.py          # FBS analysis script for Group 3
├── run_all_scripts.bat   # Batch file to run all scripts
└── README.md            # This file
```

## Data Requirements
The scripts expect input data files to be in the same directory as the Python scripts. Ensure your experimental data is properly formatted before running the analysis.

## Output
The scripts will generate visualizations and analysis results, typically saved as image files (PNG, PDF) in the same directory.

## Contributing
Please follow standard Python coding conventions and maintain consistent documentation for any new features or modifications.

## License
This project is for educational and research purposes only.