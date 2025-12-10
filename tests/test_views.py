import pytest
from django.urls import reverse
from members.models import Task

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
def test_task_list_get(client):
    Task.objects.create(title='A task')
    url = reverse('members:task_list')
    res = client.get(url)
    assert res.status_code == 200
    content = res.content.decode()
    assert 'A task' in content

@pytest.mark.django_db
def test_add_task_post(client):
    url = reverse('members:task_list')
    res = client.post(url, {'title': 'New Task'})
    # Should redirect back to list page after creation
    assert res.status_code == 302
    assert Task.objects.filter(title='New Task').exists()

@pytest.mark.django_db
def test_toggle_task(client):
    t = Task.objects.create(title='Toggle me')
    url = reverse('members:toggle_task', args=[t.pk])
    # toggle via GET is allowed by our view
    res = client.get(url)
    assert res.status_code == 302
    t.refresh_from_db()
    assert t.completed is True

@pytest.mark.django_db
def test_delete_task(client):
    t = Task.objects.create(title='Delete me')
    url = reverse('members:delete_task', args=[t.pk])
    res = client.get(url)
    assert res.status_code == 302
    assert not Task.objects.filter(pk=t.pk).exists()