from llm import ask_llm


def create_plan(project_context, user_request):

    prompt = f"""
You are a senior software engineer.

You have analyzed an existing Node.js project.

User requirement:

{user_request}

Project source code:

{project_context}

Your task:

Create a concise execution plan.

For each step include:

1. File(s) to modify
2. Why the file needs modification
3. What change should be made

Do NOT generate code.

Only create the implementation plan.
"""

    return ask_llm(prompt)

if __name__ == "__main__":

    context = """
Node.js Notes Application

Files:

server.js

note.model.js

note.routes.js

note.controller.js
"""

    request = (
        "Improve the application so users can "
        "better organise and search their notes."
    )

    plan = create_plan(context, request)

    print(plan)