import pytest
from rest_framework.test import APIClient
from members.models import Task

@pytest.mark.django_db
def test_api_create_missing_title_returns_400():
    client = APIClient()
    res = client.post('/api/tasks/', {}, format='json')
    assert res.status_code == 400
    assert 'title' in res.json()

@pytest.mark.django_db
def test_api_create_too_long_title_returns_400():
    client = APIClient()
    long_title = 'x' * 300
    res = client.post('/api/tasks/', {'title': long_title}, format='json')
    assert res.status_code == 400
    assert 'title' in res.json()

@pytest.mark.django_db
def test_api_list_returns_tasks_in_created_desc_order():
    client = APIClient()
    t1 = Task.objects.create(title='first')
    t2 = Task.objects.create(title='second')
    res = client.get('/api/tasks/')
    assert res.status_code == 200
    data = res.json()
    # ordering in the viewset queryset is -created_at, so newest (t2) should be first
    assert len(data) >= 2
    assert data[0]['id'] == t2.id
    assert data[1]['id'] == t1.id