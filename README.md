# GSoC 2026 Preparation: BIDS Data Exploration

This repository documents my learning process as I prepare for the **Google Summer of Code (GSoC) 2026** with **INCF**.

My goal is to transition from general data analysis to **Neuroinformatics**. I am using this repo to practice parsing, cleaning, and visualizing brain imaging data structures (BIDS) using Python.

## 📂 Project Focus: OpenNeuro `ds000246`
I selected the **MEG-BIDS Brainstorm data sample (ds000246)** for my initial experiments because it provides a clear structure for handling both MRI and MEG data.

### 🛠️ My Tech Stack
* **Python 3.x**
* **Pandas:** For handling `.tsv` metadata files.
* **Plotly:** (Upcoming) For interactive visualization of signal intensity.
* **PyBIDS:** To understand BIDS layout querying.

## 📊 Current Progress

### Phase 1: Data Connection & Parsing (Complete)
I created a script `bids_parser.py` to connect to the OpenNeuro API.
* **Challenge:** I initially tried loading the file as a standard CSV, but the formatting broke.
* **Solution:** I realized BIDS uses tab-separated values (`.tsv`) and updated the Pandas arguments to `sep='\t'`.
* **Result:** successfully parsed the `participants.tsv` file and added a data integrity check to ensure unique IDs.

*Note: This is a personal learning sandbox. The code here is for exploration and testing purposes.*
