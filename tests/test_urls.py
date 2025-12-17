from django.urls import reverse

def test_url_reverse_for_views():
    assert reverse('todolist:task_list') == '/'
    assert reverse('todolist:toggle_task', args=[1]) == '/toggle/1/'
    assert reverse('todolist:delete_task', args=[1]) == '/delete/1/'