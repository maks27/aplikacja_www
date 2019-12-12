from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password_compare = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_compare']
        hidden_pass = {
            'password': {'write_only : True'}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            )
        password = self.validated_data['password']
        password_compere = self.validated_data['password_compare']

        if password != password_compere:
            raise serializers.ValidationError({'password': 'Haslo zle'})
        user.set_password(password)
        user.save()
        return user
