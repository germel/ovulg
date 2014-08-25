from django.core import serializers

data = serializers.serialize("json", {'a': 'b', 'c': 'd'})
