from fastapi import FastAPI
from env import EmailEnv
from grader import grade
from baseline import baseline_agent
app = FastAPI()
env = EmailEnv()

@app.get("/")
def home():
    return {"message": "Email Triage Env Running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)

@app.get("/state")
def state():
    return env.state()

@app.get("/tasks")
def tasks():
    return ["easy", "medium", "hard"]
@app.post("/grader")
def grader_api(action: dict):
    expected = env.current["label"]
    score = grade(action, expected)
    return {"score": score}
@app.get("/baseline")
def baseline():
    obs = env.reset()
    action = baseline_agent(obs)
    return action
