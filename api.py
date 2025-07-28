from fastapi import FastAPI
from pydantic import BaseModel
from src.linkedin_copilot.crew import LinkedinCopilotCrew

app = FastAPI()

class CrewInput(BaseModel):
    topic: str
    user_persona: str

@app.get("/")
def read_root():
    return {"status": "LinkedIn Copilot API is running"}

@app.post("/kickoff")
def kickoff_crew(inputs: CrewInput):
    try:
        inputs_dict = inputs.dict()
        linkedin_crew = LinkedinCopilotCrew()
        result = linkedin_crew.crew().kickoff(inputs=inputs_dict)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
