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
            users = User.objects.all()
            users_list = list(users)

            if not users:
                return HttpResponseNotFound("No users found", status=204)
            # return render(request, 'users.html', {'users': users})
            return JsonResponse(users_list, safe=False, status=200)
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

def listUsersById(request: HttpRequest, id: int):
    """Method that will return users based on id from the database

    Args:
        request (HttpRequest): The HTTP object containing information.
        id (int): The user's ID to search for in the database.
    Returns:
        JsonResponse: A JSON response containing the user's information if
        found, or error message if user does not exist.
    """
    if request.method != 'GET':
        return JsonResponse(
            {
                'error': 'Method not allowed, GET request only'
            }, safe=False, status=405)

    try:
        user = User.objects.get(id=id)
        return JsonResponse(user, safe=False, status=200)

    except User.DoesNotExist:
        return JsonResponse(
            {
                'error': 'User not found'
            }, safe=False, status=404)
    except DatabaseError as e:
        return JsonResponse(
            {
                'error': 'Database error: ' + str(e)
            }, safe=False, status=500)
    except Exception as e:
        return JsonResponse(
            {
                'error': str(e)
            }, safe=False, status=500)
