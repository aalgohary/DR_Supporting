# Disaster Recovery Supporting Tools

This Streamlit application is designed to help manage, compare, and analyze data related to Disaster Recovery (DR) operations. It provides an interface for data comparison, searching, and future features such as data analysis and dashboard visualizations.

## Features

- **Changes Tool**: Upload old and recent data files (CSV/XLSX) and compare the differences between them.
- **Search Tool**: Upload data files and search for specific keywords or values within the dataset.
- **Extensible Structure**: New tools can be easily added to support additional Disaster Recovery operations.

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit library
- Pandas library (for handling CSV/XLSX data)

You can install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/aalgohary/DR_Supporting.git
cd DR_Supporting
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run Home.py
```

### Usage

- Navigate to the homepage to access the available tools.
- Changes Tool: Upload two files to compare differences between old and recent raw data.
- Search Tool: Upload a file to search for specific entries or keywords.
  More tools will be added in future versions.

### Roadmap

- **Analysis Tool**: Perform deeper analysis of DR data.
- **Dashboard Tool**: Visualize DR data in customizable dashboards.
- **Reporting Tool**: Generate reports from the analyzed DR data.

### Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

### Contact

For any inquiries, please contact ahmad.gohary@hpe.com.
