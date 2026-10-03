import logging
from util.User import User  

import pytest

logger = logging.getLogger(__name__)


class TestJsonPlaceholderAPI:
    @pytest.mark.smoke
    def test_get_users(self, api_client):
        response = api_client.get("https://jsonplaceholder.typicode.com/users")
        assert response.status_code == 200

        users = [
            User(item["id"], item["name"], item["email"], item["username"])
            for item in response.json()
        ]    

        assert users
        assert all(isinstance(user, User) for user in users)

        for user in users:
            if user.id == 1:
                logger.info("Found user with ID 1: %s", user)
                logger.info("User email is %s", user.email)
                logger.info("User username is %s", user.username)
                logger.info("User id is %s", user.id)
                break

    @pytest.mark.smoke
    def test_create_post(self, api_client):
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1,
        }
        response = api_client.post("https://jsonplaceholder.typicode.com/posts", json=payload)
        assert response.status_code == 201
        print(response.json())
        assert isinstance(response.json(), dict)
        assert response.json()["title"] == "foo"
        assert response.json()["body"] == "bar"
        assert response.json()["userId"] == 1

    @pytest.mark.smoke
    def test_update_post(self, api_client):
        payload = {
            "id": 1,
            "title": "new title",
            "body": "bar",
            "userId": 1,
        }
        response = api_client.put("https://jsonplaceholder.typicode.com/posts/1", json=payload)
        assert response.status_code == 200
        assert response.json()["title"] == "new title"
        assert response.json()["body"] == "bar"
        assert response.json()["id"] == 1
        assert response.json()["userId"] == 1

    @pytest.mark.smoke
    def test_delete_post(self, api_client):
        response = api_client.delete("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status_code == 200
        assert response.json() == {}