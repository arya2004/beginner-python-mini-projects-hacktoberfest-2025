# File Renamer Utility

A simple yet powerful command-line utility to batch rename files using regular expressions. This tool is perfect for organizing files by renaming them according to patterns.

## Features

- Rename multiple files at once using regex patterns
- Preview changes before applying them
- Simple command-line interface
- Safe operation with preview mode by default

## Installation

No additional dependencies are required! This script uses only Python standard library modules.

1. Clone this repository
2. Navigate to the project directory
3. Make the script executable (Unix-like systems):
   ```bash
   chmod +x main.py
   ```

## Usage

```bash
python main.py <directory> <pattern> <replacement> [--execute]
```

Arguments:
- `directory`: The directory containing files to rename
- `pattern`: Regular expression pattern to match in filenames
- `replacement`: Replacement pattern (can include regex groups)
- `--execute`: Optional flag to actually perform the renaming (without this, changes are only previewed)

### Examples

1. Preview removing spaces from filenames:
```bash
python main.py /path/to/files "\s+" "_"
```

2. Add prefix to all .txt files:
```bash
python main.py /path/to/files "^" "prefix_" --execute
```

3. Change file extension from .txt to .md:
```bash
python main.py /path/to/files "\.txt$" ".md" --execute
```

## Safety Features

- By default, the script runs in preview mode
- Checks for existing files to prevent overwrites
- Validates directory existence
- Provides clear feedback on what changes will be made

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.
