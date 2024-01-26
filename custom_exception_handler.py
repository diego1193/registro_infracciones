from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if isinstance(exc, AuthenticationFailed):
        custom_response = {
            "error": "Token inválido o expirado",
            "detail": str(exc)
        }
        return Response(custom_response, status=status.HTTP_401_UNAUTHORIZED)

    return response
