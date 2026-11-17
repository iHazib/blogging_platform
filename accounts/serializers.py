from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # a write-only field for password, so it won't be returned in the response as read. 

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'name', 'email', 'mobile', 'role') # all the fields required in the user registration to be serialized.

    def create(self, validated_data):
        user = CustomUser.objects.create_user(   # create_user method creates new user instance and save it to the db, while handling the password hashing on it's own.
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
            email=validated_data.get('email', ''), # optional field, if not provided it will be set to an empty string.
            mobile=validated_data['mobile'],  
            role=validated_data.get('role', 'reader') # 'reader' is the default role if not provided.
        )
        return user

class CustomLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Default validation (username/password check)
        data = super().validate(attrs)
        
        # Custom clean response
        response_data = {
            "message": "Login successful",
            "user": {
                "id": self.user.id,
                "username": self.user.username,
                "name": self.user.name,
                "role": self.user.role,
            },
            "tokens": {
                "access": data["access"],
                "refresh": data["refresh"]
            }
        }
        return response_data

        


