VALID_EMAIL = "new.student@mergington.edu"
UNKNOWN_ACTIVITY = "Debate Team"


def test_signup_success_returns_200(client):
    # Arrange
    activity_name = "Soccer Team"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": VALID_EMAIL})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {VALID_EMAIL} for {activity_name}"}


def test_signup_unknown_activity_returns_404(client):
    # Arrange
    activity_name = UNKNOWN_ACTIVITY

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": VALID_EMAIL})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_duplicate_student_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    duplicate_email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": duplicate_email})

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up for this activity"}
