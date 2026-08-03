# AI Coding Agent

## Overview

This project was developed as part of an AI Coding Agent assignment.

The objective was to build an AI agent that can understand an existing codebase and implement a new feature based on a user's requirement. Instead of generating code from scratch, the agent first analyzes the project, creates an implementation plan, generates the required code changes using Google's Gemini API, and updates the relevant files automatically.

Working on this project gave me a better understanding of how AI coding assistants analyze repositories and assist developers with code generation.

---

## Features

- Explores an existing project and reads its source files.
- Builds a project context for the LLM.
- Generates an implementation plan based on the user's requirement.
- Produces updated source code using Google's Gemini API.
- Automatically updates the required project files.
- Displays a summary of all modified files.
- Reports API errors if a request fails.

---

## How It Works

The project is divided into small modules, where each module is responsible for a specific task.

### Step 1 – Explore the Repository

The agent scans the project directory and reads the source files. The collected files are combined into a single project context.

### Step 2 – Create an Implementation Plan

The project context and the user's requirement are sent to the Gemini model. Based on this information, the model generates a step-by-step implementation plan.

### Step 3 – Generate Updated Code

Using the implementation plan, the agent requests the updated source code from the LLM. Only the files that need modifications are generated.

### Step 4 – Update the Project

The generated response is parsed using regular expressions, and the updated code is written back to the corresponding files. After the process is complete, the agent displays a summary of all modified files.

### Workflow

```text
               User Requirement
                       │
                       ▼
            Repository Exploration
                       │
                       ▼
            Build Project Context
                       │
                       ▼
        Implementation Planning
               (Gemini API)
                       │
                       ▼
            Code Generation
               (Gemini API)
                       │
                       ▼
         Automatic File Update
                       │
                       ▼
        Modified Files Summary
```

---

## Screenshots

### Implementation Planning

The agent analyzes the project context and creates an execution plan based on the user's requirement.

![Implementation Plan](screenshots/execution_plan.png)


### Final Execution Output

The agent generates the required changes, updates the project files automatically, and displays the execution summary.

![Final Output](screenshots/final_output.png)

---
## Project Structure

```text
AI-Coding-Agent/
│
├── screenshots/
│   ├── execution_plan.png
│   └── final_output.png
│
├── main.py          # Starts the workflow
├── explorer.py      # Reads project files
├── planner.py       # Generates the implementation plan
├── modifier.py      # Generates updated source code
├── writer.py        # Updates project files
├── llm.py           # Handles Gemini API communication
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
└── .env
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd AI-Coding-Agent
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

```bash
venv\Scripts\activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key.

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Usage

Update the project path and the feature request in `main.py`.

Example:

```python
project_path = r"G:\node-easy-notes-app-master"

user_request = (
    "Improve the application so users can better organise and search their notes."
)
```

Run the project.

```bash
python main.py
```

The agent will:

- Explore the repository.
- Create an implementation plan.
- Generate updated code.
- Modify the required files.
- Display a summary of the modified files.

---

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- python-dotenv
- Regular Expressions (Regex)

---

## Limitations

- Currently supports command-line execution.
- Depends on the Gemini API for planning and code generation.
- Tested on a small Node.js project.

---

## Future Improvements

Some improvements that can be added in the future are:

- Support additional programming languages.
- Improve prompt design for better code generation.
- Handle larger repositories more efficiently.
- Add a simple web interface.