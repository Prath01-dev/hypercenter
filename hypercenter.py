import os
import fnmatch

class HyperCenter:
    def __init__(self, base_directory='/', file_patterns=None, exclude_patterns=None):
        self.base_directory = base_directory
        self.file_patterns = file_patterns if file_patterns else ['*']
        self.exclude_patterns = exclude_patterns if exclude_patterns else []

    def search_files(self):
        matches = []
        for root, _, files in os.walk(self.base_directory):
            for pattern in self.file_patterns:
                for filename in fnmatch.filter(files, pattern):
                    file_path = os.path.join(root, filename)
                    if not any(fnmatch.fnmatch(file_path, pat) for pat in self.exclude_patterns):
                        matches.append(file_path)
        return matches

def main():
    # Example usage
    base_directory = 'C:\\'  # Root directory for search
    file_patterns = ['*.txt', '*.py']  # File types to include in search
    exclude_patterns = ['*.log', '*temp*']  # File types or names to exclude

    hc = HyperCenter(base_directory, file_patterns, exclude_patterns)
    results = hc.search_files()

    for file in results:
        print(file)

if __name__ == "__main__":
    main()