from django.contrib import admin
from members.models import Task

def test_task_model_registered_in_admin():
    # admin.site._registry keys are registered model classes
    assert Task in admin.site._registry