from rest_framework import viewsets
from members.models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Task.

    Endpoints:
    - GET /api/tasks/        -> list
    - POST /api/tasks/       -> create
    - GET /api/tasks/{id}/   -> retrieve
    - PATCH /api/tasks/{id}/ -> partial_update (use to toggle completed)
    - PUT /api/tasks/{id}/   -> update
    - DELETE /api/tasks/{id}/-> destroy
    """
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer