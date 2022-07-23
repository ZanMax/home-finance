from django.shortcuts import render
from django.views import View


class Periodic(View):
    def get(self, request):
        return render(request, "periodic_expenses/index.html")
