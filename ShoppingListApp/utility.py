import re

from rest_framework import status
from rest_framework.response import Response


class TextProcessors:
    @staticmethod
    def split_title_case(text):
        return re.sub(r"(\w)([A-Z])", r"\1 \2", text)


class ResponseProcessors:
    @staticmethod
    def success(data=None, message=None):
        return Response({
            "data": data,
            "status": True,
            "message": "Success" if message is None else message
        }, status=status.HTTP_200_OK)

    @staticmethod
    def failed(message=None):
        return Response({
            "status": False,
            "message": "Failed" if message is None else message
        }, status=status.HTTP_200_OK)
