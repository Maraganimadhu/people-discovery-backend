from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.utils import timezone
from .models import Profile

@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])   # 🔥 REQUIRED
@permission_classes([IsAuthenticated])
def my_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    print("the call successful ----------------------------")

    if request.method == 'GET':
        return Response({
            "name": profile.name,
            "age": profile.age,
            "category": profile.category,
            "bio": profile.bio,
            "last_active": profile.last_active
        })

    if int(request.data.get('age', 18)) < 18:
        return Response({"error": "Age must be 18+"}, status=400)

    profile.name = request.data.get('name', profile.name)
    profile.age = request.data.get('age', profile.age)
    profile.category = request.data.get('category', profile.category)
    profile.bio = request.data.get('bio', profile.bio)
    profile.last_active = timezone.now()
    profile.save()

    return Response({"message": "Profile updated"})
