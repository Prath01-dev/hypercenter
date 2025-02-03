# HyperCenter

HyperCenter is a Python program designed to search for files across all drives on Windows systems with advanced filtering options. This tool can streamline searches by including or excluding specific file patterns.

## Features

- Search across specified directories and their subdirectories.
- Filter search results based on file patterns (e.g., `*.txt`, `*.py`).
- Exclude files from search results based on patterns (e.g., `*.log`, `*temp*`).

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/hypercenter.git
   ```
2. Navigate to the project directory.
   ```bash
   cd hypercenter
   ```

## Usage

1. Open the `hypercenter.py` file in a text editor.
2. Modify the `base_directory`, `file_patterns`, and `exclude_patterns` variables as needed:
   - `base_directory`: Set this to the root directory where you want to start your search (e.g., `'C:\\'`).
   - `file_patterns`: List of file patterns to search for (e.g., `['*.txt', '*.py']`).
   - `exclude_patterns`: List of file patterns to exclude from the search (e.g., `['*.log', '*temp*']`).

3. Run the script with Python:
   ```bash
   python hypercenter.py
   ```

4. The program will print the paths of files that match the search criteria to the console.

## Contributing

Feel free to fork this project, submit issues, and send pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Inspired by the need for efficient file searching with customizable filtering options on Windows platforms.