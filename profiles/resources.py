from import_export import resources
from .models import Requests, Reports

class RequestResource(resources.ModelResource):
    class Meta:
        model = Requests
        fields = ['sender', 'receiver', 'sender_username', 'receiver_username', 'document_type', 'purpose', 'date_created', 'id']

    
    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            if h == 'sender':
                headers[i] = "sender_id"
            if h == 'receiver':
                headers[i] = "receiver_id"
        return headers


class ReportResource(resources.ModelResource):
    class Meta:
        model = Reports
        fields = ['sender', 'receiver', 'sender_username', 'receiver_username', 'location', 'message', 'date_created', 'id']


    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            if h == 'sender':
                headers[i] = "sender_id"
            if h == 'receiver':
                headers[i] = "receiver_id"
        return headers