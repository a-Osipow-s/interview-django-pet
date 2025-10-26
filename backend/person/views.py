from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response

from person.models import Person, Role


# serializers
class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        depth = kwargs.pop('depth', None)
        super().__init__(*args, **kwargs)
        
        if depth is not None:
            self.Meta.depth = min(depth, 9)


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        depth = kwargs.pop('depth', None)
        super().__init__(*args, **kwargs)
        
        if depth is not None:
            self.Meta.depth = min(depth, 9)


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        self.get_serializer(queryset, many=True)
        result_items = []
        for person in queryset:
            result_items.append(
                {
                    'bio': person.bio,
                    'company': person.company,
                    'job_title': person.job_title,
                    'user': {
                        'email': person.user.email,
                        'first_name': person.user.first_name,
                        'last_name': person.user.last_name,
                        'username': person.user.username,
                    }
                }
            )

        return Response(result_items, status=status.HTTP_200_OK)


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all().order_by('-created_at')
    serializer_class = RoleSerializer