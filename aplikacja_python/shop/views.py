from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from shop.models import Users, Products, Orders, Order_products, Categories
from shop.serializers import UserSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Users.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request1, pk):
    """
            Retrieve, update or delete a code snippet.
            """
    try:
        snippet = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=404)

    if request1.method == 'GET':
        serializer = UserSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request1.method == 'PUT':
        data = JSONParser().parse(request1)
        serializer = UserSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request1.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
