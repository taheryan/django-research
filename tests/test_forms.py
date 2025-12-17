import pytest
from todolist.forms import TaskForm

def test_task_form_valid():
    form = TaskForm(data={'title': 'Do homework'})
    assert form.is_valid()

def test_task_form_invalid_blank():
    form = TaskForm(data={'title': ''})
    assert not form.is_valid()
    assert 'title' in form.errors

def test_task_form_invalid_only_spaces():
    # forms.CharField default strip=True will turn '   ' into ''
    form = TaskForm(data={'title': '   '})
    assert not form.is_valid()
    assert 'title' in form.errors