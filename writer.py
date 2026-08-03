import os
import re


def write_generated_files(generated_text, project_path):

    pattern = r"FILE:\s*(.*?)\s*```(?:\w+)?\s*(.*?)```"

    matches = re.findall(
        pattern,
        generated_text,
        re.DOTALL | re.IGNORECASE
    )

    if not matches:
        print("No files found to write.")
        return

    modified_files = []

    print("\nWriting generated files...\n")

    for relative_path, code in matches:

        relative_path = relative_path.strip()
        code = code.strip()

        full_path = os.path.join(
            project_path,
            relative_path
        )

        os.makedirs(
            os.path.dirname(full_path),
            exist_ok=True
        )

        with open(
            full_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(code)

        modified_files.append(relative_path)

        print(f"Updated: {relative_path}")

    print("\nFinished writing all generated files.")

    print("\nMODIFIED FILES SUMMARY")

    for file in modified_files:
        print(f"- {file}")

    print(f"Total files modified: {len(modified_files)}")