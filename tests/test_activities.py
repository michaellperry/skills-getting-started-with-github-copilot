def test_get_activities_returns_200(client):
    # Arrange
    activities_path = "/activities"

    # Act
    response = client.get(activities_path)

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_expected_activity_data(client):
    # Arrange
    activities_path = "/activities"

    # Act
    response = client.get(activities_path)
    payload = response.json()

    # Assert
    assert "Chess Club" in payload
    assert payload["Chess Club"]["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert isinstance(payload["Chess Club"]["participants"], list)
