from import_export import resources
from .models import Requests, Reports, WalkInRequests

class RequestResource(resources.ModelResource):
    class Meta:
        model = Requests
        fields = ['sender_username', 'receiver_username', 'document_type', 'purpose', 'date_created']



class WalkInRequestResource(resources.ModelResource):
    class Meta:
        model = WalkInRequests
        fields = ['owner__first_name', 'document_type', 'purpose', 'date_created']

    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            if h == 'owner__first_name':
                headers[i] = "Name"
        return headers


class ReportResource(resources.ModelResource):
    class Meta:
        model = Reports
        fields = ['sender_username', 'receiver_username', 'location', 'message', 'date_created']