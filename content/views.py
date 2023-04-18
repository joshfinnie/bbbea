from django.core.exceptions import BadRequest
from django.http import Http404

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from content.serializers import ObjectSerializer, BatchSerializer
from content.models import Object


class ObjectList(APIView):
    def get(self, request):
        key = request.GET.get("key")
        value = request.GET.get("value")
        if key and not value:
            data = Object.objects.filter(data__contains=[{"key": key}])
        elif not key and value:
            data = Object.objects.filter(data__contains=[{"value": value}])
        elif key and value:
            data = Object.objects.filter(data__contains=[{"key": key, "value": value}])
        else:
            data = Object.objects.all()

        serializer = ObjectSerializer(data, many=True)

        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ObjectDetail(APIView):
    def get(self, request, object_id):
        try:
            data = Object.objects.get(object_id=object_id)
        except Object.DoesNotExist:
            raise Http404
        serializer = ObjectSerializer(data)
        return Response(serializer.data)
