import os

from django.http import HttpResponse, StreamingHttpResponse
from rest_framework.decorators import APIView
from wsgiref.util import FileWrapper

from .Helpers import OptimizedExport


# Create your views here.


class ExportOrder(APIView):
    def get(self, request):
        export = OptimizedExport()
        status, file_path = export.make_query()

        if status:
            response = StreamingHttpResponse(FileWrapper(open(file_path, 'rb')), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="order_export.csv"'
            response['Content-Length'] = os.path.getsize(file_path)
            return response

        return HttpResponse("<h2>Failed to generate export</h2>")