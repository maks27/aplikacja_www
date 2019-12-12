from rest_framework import serializers
from django.contrib.auth.models import User
import re
from django.utils.translation import ugettext as _


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
        if not re.findall('\d', password):
            raise serializers.ValidationError(
                _("Hasło musi posiadać co najmniej 1 liczbe"),
                code='password_no_number',
            )

        if len(password) < 8:
            raise serializers.ValidationError(_("Hasło musi posiadać co najmniej 8 znaków"), code='too_short', )

        user.set_password(password)
        user.save()
        return user
