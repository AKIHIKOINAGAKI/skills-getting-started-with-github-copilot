def test_root_redirects_to_static_index(client):
    # Arrange
    follow_redirects = False

    # Act
    response = client.get("/", follow_redirects=follow_redirects)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"