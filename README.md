# Data Center Water Scarcity Analysis

## Table of Contents

- [Data Center Water Scarcity Analysis](#data-center-water-scarcity-analysis)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Problem Statement](#problem-statement)
    - [Project structure](#project-structure)
  - [System Requirements](#system-requirements)
  - [Installation Guide](#installation-guide)
  - [Demo (Quickstart)](#demo-quickstart)
  - [Instructions for Use](#instructions-for-use)
    - [Running on Custom Data](#running-on-custom-data)
    - [Reproducing Paper Results](#reproducing-paper-results)
  - [Data Sources](#data-sources)
  - [License](#license)
  - [Contact](#contact)

## Overview

This study analyzes the water use of data centers using spatial GIS modeling and environmental footprinting methodologies, and assesses their impact on local water scarcity.

See the [pyproject.toml](pyproject.toml) file for complete package information such as project metadata and dependencies.

The input data for this project is available on Zenodo: [![DOI](https://zenodo.org/records/20763321)](https://doi.org/10.5281/zenodo.14914471)


### Problem Statement

Data centers require significant water resources for cooling systems and power generation, yet the global scale and distribution is still unknown. With water scarcity risks growing as global warming rises, data centers are increasingly vulnerable, while contributing to local water stress. This project analyzes their vulnerability and contributions to local water scarcity through:

- Web scraping of facility data
- Estimating water and energy use metrics
- Modeling water scarcity under climate change scenarios
- Assessing the impact of data centers on water scarcity

### Project structure

```bash
├── data
│   ├── inputs                              # See Zenodo link for input data
│   └── outputs                             # See Zenodo link for output data
├── functions
│   ├── data_etl                            # Module for data cleaning and transformation functions
│   ├── energy_and_water_use                # Module for energy and water use analysis functions
│   ├── figures                             # Module for creating figures functions
│   ├── water_scarcity                      # Module for water scarcity assessment functions
│   └── project_settings.py                 # Project-wide variables
├── 1_data_etl.ipynb                        # Data cleaning and transformation notebook
├── 2_energy_and_water_use_analysis.ipynb   # Energy and water use analysis notebook
├── 3_water_scarcity_assessment.ipynb       # Water scarcity assessment notebook
├── 4_figures.ipynb                         # Figures notebook
├── demo_workflow.ipynb                     # ⚡ Standalone demo (< 5s) with simulated data
├── LICENSE                                 # License file
├── README.md                               # This file
└── pyproject.toml                          # Project metadata and dependencies
```

## System Requirements

- **Operating Systems**: Tested on macOS (Sonoma 14, Sequoia 15) and Linux (Ubuntu 22.04). Compatible with Windows 11.
- **Python Version**: Python >= 3.13.
- **Dependencies**: Managed via [uv](https://docs.astral.sh/uv/) and listed in [pyproject.toml](pyproject.toml) (including `geopandas >= 1.0.1`, `rasterio >= 1.4.3`, `pandas >= 2.2.3`, `numpy >= 2.2.2`, `cartopy >= 0.24.1`, `statsmodels >= 0.14.4`).
- **Hardware Requirements**: Standard desktop or laptop computer (>= 8 GB RAM). No GPU or non-standard hardware required.

## Installation Guide

1. Install `uv` (recommended package manager):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/amwientjes/<data-center-water-scarcity>
   cd <data-center-water-scarcity>
   ```
3. Install dependencies in an isolated virtual environment:
   ```bash
   uv sync
   ```
- **Typical install time**: ~1–2 minutes on a standard desktop computer.

## Demo (Quickstart)

A standalone minimal working example using simulated data (`data/inputs/demo/`):

- **How to run**:
  - In Jupyter / VS Code: Open [demo_workflow.ipynb](demo_workflow.ipynb) and select the `.venv` kernel.
  - From terminal:
    ```bash
    uv run python -m nbconvert --execute --inplace demo_workflow.ipynb
    ```
- **Expected run time**: < 5 seconds on a standard desktop computer.
- **Expected output**: Formatted tabular outputs demonstrating direct/indirect water footprints, extraction site clustering, Environmental Flow Requirements (VMF method), and seasonal water scarcity indicators (confirming the tipping effect: baseline water scarcity increasing from 3 to 5 months in the arid basin).

## Instructions for Use

### Running on Custom Data
To evaluate custom facilities, provide a dataset containing:
- `critical_power_mw`: IT power capacity (MW)
- `latitude`, `longitude`: Geographic coordinates (WGS84)
- `cooling_tech` / `ashrae_zone`: Cooling system configuration or ASHRAE climate zone
- `power_grid_zone`: Regional power grid identifier

### Reproducing Paper Results
1. Download baseline input files from [Zenodo](https://doi.org/10.5281/zenodo.14914472) into `data/inputs/`.
2. Launch Jupyter Lab: `uv run jupyter lab`
3. Run [3_water_scarcity_assessment.ipynb](3_water_scarcity_assessment.ipynb) to model water extraction sites and scarcity across climate scenarios.
4. Run [4_figures.ipynb](4_figures.ipynb) to reproduce paper figures and statistical summaries.

## Data Sources

The input data for this project is available on Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14914472.svg)](https://doi.org/10.5281/zenodo.14914472)

**Note on data anonymization:** To comply with proprietary data restrictions, only the input data for the last two scripts (`3_water_scarcity_assessment.ipynb` and `4_figures.ipynb`) has been provided. This ensures the anonymization of individual data center locations and specifications.

## License

The code in this repository is licensed under the GNU AGPLv3 License. See the [LICENSE](LICENSE) file for details.

## Contact

For further inquiries, please contact the author through LinkedIn: [Audrey Wientjes](https://www.linkedin.com/in/audrey-wientjes/)
