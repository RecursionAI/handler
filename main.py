from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main():
    return {"message": "Welcome to Handler"}


@app.post("v1/chat/completions")
def chat_completions():

