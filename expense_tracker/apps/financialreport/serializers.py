from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import ExpenseIncome
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError({'error': 'User account is disabled.'})
                return user
            raise serializers.ValidationError({'error': 'Unable to log in with provided credentials.'})
        raise serializers.ValidationError({ "error": "Must include 'username' and 'password'."})

class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = ExpenseIncome
        fields = [
            'id', 'user', 'title', 'description', 'amount', 
            'transaction_type', 'tax', 'tax_type', 'created_at', 
            'updated_at', 'total'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'total']
    
    def get_total(self, obj):
        return obj.total
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError({'error': 'Amount must be positive.'})
        return value
    
    def validate_tax(self, value):
        if value < 0:
            raise serializers.ValidationError({'eror': 'Tax cannot be negative.'})
        return value
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)