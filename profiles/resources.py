from import_export import resources
from .models import Requests, Reports

class RequestResource(resources.ModelResource):
    class Meta:
        model = Requests
        fields = ['sender_username', 'receiver_username', 'document_type', 'purpose', 'date_created']



class ReportResource(resources.ModelResource):
    class Meta:
        model = Reports
        fields = ['sender_username', 'receiver_username', 'location', 'message', 'date_created']