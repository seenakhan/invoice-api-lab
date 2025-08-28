# invoice-api-lab


### 1. Project Overview
- Brief description of the lab’s purpose  
- Technologies used (Python, FastAPI, GitHub Copilot)  
- Target audience (professional developers, Copilot learners)

```md
## Invoice API Lab with FastAPI & GitHub Copilot
This lab helps developers explore AI-assisted coding workflows using GitHub Copilot. You'll build and test a FastAPI-based invoice processor, refactor Python modules, and compare autocomplete vs edit mode.
```

### 2. Objectives
- What learners will achieve  
- Skills they’ll practice

```md
##  Objectives
- Extend and refactor Python modules using Copilot
- Build and test FastAPI endpoints
- Compare autocomplete vs edit mode workflows
```

### 3. ⚙️ Setup Instructions
- How to install dependencies  
- How to run the app locally  
- Any environment variables or ports

```md
##  Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 4. Copilot Prompts
- Suggested prompts for learners to try  
- Tips for using autocomplete and edit mode

```md
## Copilot Prompts
- “Add authentication to the invoice API”
- “Write unit tests for apply_late_fee and to_json”
- “Refactor is_overdue to accept a reference date”
```

### 5. Testing Instructions
- How to run unit tests  
- What to expect from test coverage

```md
## Testing
```bash
pytest tests/
```
### 6. Reflection Questions
- Encourage learners to think critically about Copilot’s suggestions

```md
## Reflection
- Which mode supported deeper reasoning?
- How did Copilot handle edge cases?
- What would you change in a production PR?
```

### 7. Multilingual Support (Optional)
- Link to translated README files  
- Note on cultural adaptation

```md
##  Other Languages
- [Arabic README](README.ar.md)
- [French README](README.fr.md)
```

### 8. Feedback Endpoint (Optional)
- How learners can submit feedback via API

```md
## Feedback
POST your reflections to `/feedback/`:
```bash
curl -X POST http://localhost:8000/feedback/ -H "Content-Type: application/json" -d '{"copilot_used": true, "insights": "Edit mode helped me refactor faster."}'
```

