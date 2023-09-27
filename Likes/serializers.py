from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'created_at', 'owner', 'post'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
        
    