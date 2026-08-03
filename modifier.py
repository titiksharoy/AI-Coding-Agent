from llm import ask_llm


def generate_code(project_context, execution_plan, user_request):

    prompt = f"""
You are a senior Node.js software engineer.

You are modifying an existing Node.js project.

User Requirement:

{user_request}

Execution Plan:

{execution_plan}

Project Source Code:

{project_context}

Your task:

Implement the requested feature.

Rules:

1. Preserve existing functionality.
2. Modify only the necessary files.
3. Return the COMPLETE updated code for each modified file.
4. Clearly separate each file.

Use this format:

FILE: app/models/note.model.js
```javascript
<complete file>
```

FILE: app/controllers/note.controller.js
```javascript
<complete file>
```

FILE: app/routes/note.routes.js
```javascript
<complete file>
```
"""

    return ask_llm(prompt)


if __name__ == "__main__":

    project = """
Node.js Notes Application

Files:
server.js
note.model.js
note.controller.js
note.routes.js
"""

    plan = """
1. Add tags field
2. Add search endpoint
3. Update controller
"""

    request = (
        "Improve the application so users can "
        "better organise and search their notes."
    )

    result = generate_code(
        project,
        plan,
        request
    )

    print(result)