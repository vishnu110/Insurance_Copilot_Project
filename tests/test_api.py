from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_chat():

    response = client.post(
        "/chat",
        json={
            "message":
                "Suggest insurance for diabetic patient"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "assistant_response" in data