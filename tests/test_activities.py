from src.app import activities


def test_get_activities_returns_all_activity_details(client):
    # Arrange
    expected_activity_names = set(activities)
    expected_fields = {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    response_activities = response.json()
    assert set(response_activities) == expected_activity_names
    for activity in response_activities.values():
        assert set(activity) == expected_fields
        assert isinstance(activity["participants"], list)
        assert all(isinstance(email, str) for email in activity["participants"])
        assert isinstance(activity["max_participants"], int)