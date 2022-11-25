from import_export import resources
from .models import Requests, Reports

class RequestResource(resources.ModelResource):
    class Meta:
        model = Requests


class ReportResource(resources.ModelResource):
    class Meta:
        model = Reports