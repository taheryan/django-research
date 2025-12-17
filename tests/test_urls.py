from django.urls import reverse

def test_url_reverse_for_views():
    assert reverse('members:task_list') == '/'
    assert reverse('members:toggle_task', args=[1]) == '/toggle/1/'
    assert reverse('members:delete_task', args=[1]) == '/delete/1/'