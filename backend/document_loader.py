import os
from typing import List, Dict


def load_documents(folder_path: str) -> List[Dict]:
    """
    Load text documents from a folder recursively.

    Returns:
        List of dictionaries containing:
        - content
        - source file name
        - file path
    """

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    documents = []

    for root, _, files in os.walk(folder_path):

        for file in files:

            if file.endswith(".txt"):

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:

                        content = f.read()

                        documents.append(
                            {
                                "content": content,
                                "source": file,
                                "path": file_path,
                            }
                        )

                except Exception as e:
                    print(f"Failed to load {file_path}: {e}")

    return documents