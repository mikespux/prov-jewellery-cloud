"""
Validations API views
"""
from rest_framework import viewsets
from ..models import Validation, WorkInProgress
from .validation_serializer import ValidationSerializer
from .wip_serializer import WorkInProgressSerializer


class ValidationView(viewsets.ModelViewSet):
    """Return validations"""
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer


class WorkInProgressView(viewsets.ModelViewSet):
    """Return wip's"""
    queryset = WorkInProgress.objects.all()
    serializer_class = WorkInProgressSerializer