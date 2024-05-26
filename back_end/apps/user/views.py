from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.http import HttpResponseNotFound
from .models import User
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def listUsers(request: HttpRequest):
    """Method that will return a list of users from db

    Args:
        request (HttpRequest): The HTTP request object containing information
        the incoming request.
    """
    if request.method == 'GET':
        try:
            users = list(User.objects.all())
            if not users:
                return HttpResponseNotFound("No users found", status=204)
            # return render(request, 'users.html', {'users': users})
            return JsonResponse(users, safe=False)
        except DatabaseError as e:
            return JsonResponse(
                {
                    'error': 'Database error: ' + str(e)
                },
                status=500)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'No users found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse(
            {
                'error': 'Method not allowed, GET request only'
            },
            status=405)
