from fastapi.testclient import TestClient

from app import app, health_check


def test_health_check_returns_ok() -> None:
    assert health_check() == {"status": "ok"}


def test_health_route_returns_ok() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
