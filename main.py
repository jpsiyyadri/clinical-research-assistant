from fastapi import FastAPI

app = FastAPI(
    title="Sample FastAPI Application",
    description="A simple FastAPI project set up with uv package manager",
    version="0.1.0"
)

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the application is running.
    """
    return {"status": "healthy"}