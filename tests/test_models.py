import pytest
from members.models import Task

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_task_str_and_defaults():
    t = Task.objects.create(title='Buy milk')
    assert str(t) == 'Buy milk'
    assert t.completed is False
    assert t.pk is not None