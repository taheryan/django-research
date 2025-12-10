import pytest
from rest_framework.test import APIClient
from members.models import Task

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_api_list_and_create():
    client = APIClient()
    # Initially no tasks
    res = client.get('/api/tasks/')
    assert res.status_code == 200
    assert res.json() == []

    # Create a task
    res = client.post('/api/tasks/', {'title': 'API Task'}, format='json')
    assert res.status_code == 201
    data = res.json()
    assert data['title'] == 'API Task'
    assert data['completed'] is False
    task_id = data['id']
    assert Task.objects.filter(pk=task_id).exists()

@pytest.mark.django_db
def test_api_toggle_and_delete():
    client = APIClient()
    t = Task.objects.create(title='Toggle me')
    # Partial update (toggle)
    res = client.patch(f'/api/tasks/{t.pk}/', {'completed': True}, format='json')
    assert res.status_code == 200
    t.refresh_from_db()
    assert t.completed is True

    # Delete
    res = client.delete(f'/api/tasks/{t.pk}/')
    assert res.status_code == 204
    assert not Task.objects.filter(pk=t.pk).exists()