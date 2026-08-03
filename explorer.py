import os


def explore_project(project_path):

    project_files = []

    for root, dirs, files in os.walk(project_path):

        # ignore unnecessary folders
        dirs[:] = [
            d for d in dirs 
            if d not in ["node_modules", ".git"]
        ]

        for file in files:

            if file.endswith((".js", ".json", ".md")):

                file_path = os.path.join(root, file)

                try:
                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                    project_files.append({
                        "path": file_path,
                        "content": content
                    })

                except Exception as e:
                    print(
                        "Could not read:",
                        file_path,
                        e
                    )

    return project_files



if __name__ == "__main__":

    project_path = r"G:\node-easy-notes-app-master"

    files = explore_project(project_path)


    print("\nFiles analysed:\n")


    for file in files:

        print("======================")
        print(file["path"])
        print("======================")

        print(
            file["content"][:500]
        )

        print("\n")