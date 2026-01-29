from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from profiles.models import Profile
from interactions.models import Interaction

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def discover_people(request):
    last_24_hours = timezone.now() - timedelta(hours=24)

    interacted_users = Interaction.objects.filter(
        from_user=request.user
    ).values_list('to_user_id', flat=True)

    profiles = Profile.objects.filter(
        last_active__gte=last_24_hours
    ).exclude(
        user=request.user
    ).exclude(
        user__id__in=interacted_users
    ).order_by('-last_active')

    data = []
    for p in profiles:
        data.append({
            "id": p.user.id,
            "name": p.name,
            "age": p.age,
            "category": p.category,
            "bio": p.bio
        })

    return Response(data)
