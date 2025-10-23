#!/usr/bin/env python3

import os
import re
from pathlib import Path
import argparse
from typing import List, Optional

class FileRenamer:
    def __init__(self, directory: str):
        """Initialize FileRenamer with target directory."""
        self.directory = Path(directory)
        if not self.directory.exists():
            raise ValueError(f"Directory '{directory}' does not exist")

    def get_files(self, pattern: Optional[str] = None) -> List[Path]:
        """Get list of files matching the pattern in the directory."""
        files = []
        for file in self.directory.iterdir():
            if file.is_file():
                if pattern is None or re.search(pattern, file.name):
                    files.append(file)
        return files

    def rename_files(self, pattern: str, replacement: str, preview: bool = True) -> List[tuple]:
        """
        Rename files based on pattern and replacement.
        Returns list of tuples with (old_name, new_name).
        """
        files = self.get_files()
        changes = []

        for file in files:
            new_name = re.sub(pattern, replacement, file.name)
            if new_name != file.name:
                new_path = file.parent / new_name
                changes.append((str(file), str(new_path)))
                if not preview:
                    if not new_path.exists():
                        file.rename(new_path)
                    else:
                        print(f"Warning: Cannot rename '{file.name}' to '{new_name}' - destination exists")

        return changes

def main():
    parser = argparse.ArgumentParser(description='Batch rename files using regex patterns')
    parser.add_argument('directory', help='Directory containing files to rename')
    parser.add_argument('pattern', help='Regex pattern to match in filenames')
    parser.add_argument('replacement', help='Replacement pattern')
    parser.add_argument('--execute', action='store_true', help='Execute renaming (default is preview only)')

    args = parser.parse_args()

    try:
        renamer = FileRenamer(args.directory)
        changes = renamer.rename_files(args.pattern, args.replacement, preview=not args.execute)

        if changes:
            print(f"{'Preview of changes:' if not args.execute else 'Executing changes:'}")
            for old, new in changes:
                print(f"  {os.path.basename(old)} -> {os.path.basename(new)}")
            if not args.execute:
                print("\nRun with --execute to apply changes")
        else:
            print("No files match the pattern")

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
