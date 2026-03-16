VALID_EMAIL = "michael@mergington.edu"
UNKNOWN_ACTIVITY = "Debate Team"
MISSING_EMAIL = "not.enrolled@mergington.edu"


def test_unregister_success_returns_200(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": VALID_EMAIL})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {VALID_EMAIL} from {activity_name}"}


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity_name = UNKNOWN_ACTIVITY

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": VALID_EMAIL})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_student_not_signed_up_returns_404(client):
    # Arrange
    activity_name = "Soccer Team"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": MISSING_EMAIL})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}
