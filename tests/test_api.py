import json
import requests


def test_create_repository(get_git_token, get_repo_name):
    url = 'https://api.github.com/user/repos'
    headers = {
        'Authorization': f'token {get_git_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'name': get_repo_name,
        'description': "Тестовый репозиторий",
        'private': True
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    assert response.status_code == 201, f"Ошибка при создании репозитория: {response.status_code}"


def test_delete_repository(get_git_token, get_repo_name, get_user_name):
    url = f'https://api.github.com/repos/{get_user_name}/{get_repo_name}'
    headers = {
        'Authorization': f'token {get_git_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204, f"Ошибка при удалении репозитория: {response.status_code}"
