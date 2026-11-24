"""FastAPI application for the MLOps project."""

from fastapi import FastAPI

app = FastAPI(title="MLOps 2 API")


def health_check() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "ok"}


@app.get("/health")
def get_health() -> dict[str, str]:
    """Expose the health status over HTTP."""
    return health_check()
