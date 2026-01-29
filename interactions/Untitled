from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Interaction

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_interaction(request):
    to_user_id = request.data.get('to_user')
    interaction_type = request.data.get('interaction_type')

    if interaction_type not in ['INTEREST', 'SKIP']:
        return Response({"error": "Invalid interaction type"}, status=400)

    if request.user.id == int(to_user_id):
        return Response({"error": "Cannot interact with yourself"}, status=400)

    try:
        to_user = User.objects.get(id=to_user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    if Interaction.objects.filter(from_user=request.user, to_user=to_user).exists():
        return Response({"error": "Already interacted"}, status=400)

    Interaction.objects.create(
        from_user=request.user,
        to_user=to_user,
        interaction_type=interaction_type
    )

    return Response({"message": "Interaction saved"})
