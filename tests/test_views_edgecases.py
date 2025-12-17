import pytest
from django.urls import reverse
from members.models import Task

@pytest.mark.django_db
def test_post_empty_title_shows_form_error_and_no_task_created(client):
    url = reverse('todolist:task_list')
    res = client.post(url, {'title': ''})
    # invalid form should re-render page with errors (status 200)
    assert res.status_code == 200
    content = res.content.decode()
    assert 'This field is required' in content or 'required' in content.lower()
    assert Task.objects.count() == 0

@pytest.mark.django_db
def test_delete_nonexistent_returns_404(client):
    url = reverse('todolist:delete_task', args=[99999])
    res = client.get(url)
    assert res.status_code == 404

@pytest.mark.django_db
def test_toggle_nonexistent_returns_404(client):
    url = reverse('todolist:toggle_task', args=[99999])
    res = client.get(url)
    assert res.status_code == 404