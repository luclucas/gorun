from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello_google():
    return "Hello google run"