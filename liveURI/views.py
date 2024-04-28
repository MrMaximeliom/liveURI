from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def callback(request):
    if request.method == 'GET':
        authorization_code = request.GET.get('code')
        # Process the authorization code and perform further actions
        return HttpResponse('Authorization code received: {}'.format(authorization_code))
    else:
        return HttpResponse(status=405)