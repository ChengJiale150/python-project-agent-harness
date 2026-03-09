from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="fastapi_test",
    description="FastAPI Test",
    version="0.1.0",
)

@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint for the API."""
    return {"message": "Hello from fastapi_test!"}

@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}

def main() -> None:
    """Entry point for the project."""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
