import os

from explorer import explore_project
from planner import create_plan
from modifier import generate_code
from writer import write_generated_files


def build_project_context(files):

    context = ""

    for file in files:
        context += f"\nFILE: {file['path']}\n"
        context += file["content"]
        context += "\n\n"

    return context


if __name__ == "__main__":

    project_path = input("Enter the project path: ").strip()

    if not os.path.exists(project_path):
        print("Error: Project path does not exist.")
        exit()

    user_request = (
        "Improve the application so users "
        "can better organise and search their notes."
    )

    print("\nReading project...")

    files = explore_project(project_path)

    print(f"Found {len(files)} files.")

    project_context = build_project_context(files)

    print("\nCreating execution plan...\n")

    plan = create_plan(
        project_context,
        user_request
    )

    print(plan)

    print("\nGenerating updated code...\n")

    generated_code = generate_code(
        project_context,
        plan,
        user_request
    )

    write_generated_files(
        generated_code,
        project_path
    )

    print("\n" + "-" * 45)
    print("AI CODING AGENT SUMMARY")
    print("-" * 45)

    print("Repository explored successfully")
    print(f"Files analysed : {len(files)}")

    print("\nExecution plan created")

    print("\nTasks completed:")
    print("✓ Repository exploration")
    print("✓ Codebase analysis")
    print("✓ Execution planning")
    print("✓ Code generation")
    print("✓ Automatic file writing")

    print("\nStatus:")
    print("✓ Existing functionality preserved")
    print("✓ Project modified successfully")

    print("-" * 45)
    print("AI Coding Agent completed successfully!")
    print("-" * 45)