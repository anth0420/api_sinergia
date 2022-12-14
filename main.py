from fastapi import FastAPI
import uvicorn
from routes import router
app = FastAPI()

app.include_router(router)

if __name__=="__main__":
    uvicorn.run("main:app", port=5000,reload=True)