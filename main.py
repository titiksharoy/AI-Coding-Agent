from explorer import explore_project
from llm import ask_llm


project_path = r"G:\node-easy-notes-app-master"

print("Reading project...")

files = explore_project(project_path)

print(f"Found {len(files)} files.")


context = ""

for file in files:

    context += f"\n\nFILE: {file['path']}\n"

    context += file["content"]


prompt = f"""
You are a senior software engineer.

Analyze this Node.js project.

Answer the following:

1. What framework is used?
2. What database is used?
3. What is the purpose of this application?
4. List the REST APIs available.
5. Explain the project structure.

Project:

{context}
"""


print("\nSending project to Gemini...\n")

answer = ask_llm(prompt)

print(answer)