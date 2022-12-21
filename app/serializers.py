from rest_framework import serializers

from .models import Entity, Property, User


class EntitySerializer(serializers.ModelSerializer):
    """
        Serializer for Entity model
    """
    modified_by = serializers.PrimaryKeyRelatedField(read_only=True, source='modified_by.username')
    value = serializers.IntegerField()
    properties = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Entity
        fields = ['modified_by','value', 'properties']

    def to_representation(self, instance):
        """
            Transform 'properties' output to a dictionary
        """
        data = super().to_representation(instance)
        properties = data.pop('properties')
        properties_dict = {}

        for property_pk in properties:
            property = Property.objects.get(pk=property_pk)
            properties_dict[property.key] = property.value
            
        data['properties'] = properties_dict
        return data

    def to_internal_value(self, data):
        """
            Map 'data[value]' to 'value'
        """
        data = data.copy()
        try:
            value = data.pop('data[value]')
            data['value'] = value
            
        except KeyError:
            pass
        return super().to_internal_value(data)