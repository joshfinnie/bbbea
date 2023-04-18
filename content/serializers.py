from rest_framework import serializers

from content.models import Object


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = "__all__"


class BatchSerializer(serializers.Serializer):
    batch_id = serializers.CharField(max_length=200)
    objects = ObjectSerializer(many=True)

    def create(self, validated_data):
        batch_id = validated_data.get("batch_id")
        objs = validated_data.get("objects", [])
        data = []
        for obj in objs:
            created_obj = Object.objects.create(batch_id=batch_id, **obj)
            data.append(created_obj)

        return {"batch_id": batch_id, "objects": data}
