from fastapi import FastAPI
from app.api import router as app_router

app = FastAPI()

# Register the contact API router
app.include_router(app_router, prefix="/api")

# Run the server (if running with `python app/main.py`)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
