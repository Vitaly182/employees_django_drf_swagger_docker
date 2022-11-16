from rest_framework import generics, filters
from .serializers import EmployeesSerializer
from .models import Employee


class SearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class EmployeesApi(generics.ListAPIView):
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    ordering_fields = ('__all__')
    search_fields = ['surname', 'name', 'patronymic', 'position__name', 'birthday', 'phone']


class EmployeesDetailApi(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
