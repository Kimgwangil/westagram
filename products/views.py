import json
from unicodedata import category
from django.views import View
from django.http  import JsonResponse
from .models import Product


# http://localhost:8000/products Get

class ProductView(View):
    def get(self, request):
        products = Product.objects.all()

        result = []

        for product in products:
            s = {
                "id" : product.id,
                "name" : product.name
            }
            result.append(s)


        return JsonResponse({ "result" : result }, status=200)

    def post(self, request):
        data = json.loads(request.body)  # json -> python

        Product.objects.create(name = data["name"], category_id = data["category_id"])

        return JsonResponse({"result": data}, status = 201)