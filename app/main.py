import uvicorn
from fastapi import FastAPI


app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=5000)
