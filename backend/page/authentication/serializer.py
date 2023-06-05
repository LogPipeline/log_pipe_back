from typing import * 
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import AdminUser
from argon2.exceptions import VerifyMismatchError
from argon2 import PasswordHasher


# 회원 가입 및 정보 수정 일원화 
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        fields: List[str] = ["id", "name", "email", "password", "password2"]
        extra_kwargs: Dict = {
            'password' : {
                'write_only': True,
                "style": {"input_type": "password"}
            }
        }
    
    def validate_password2(self, data: str) -> str:
        if self.initial_data["password"] == data:
            return data
        raise ValidationError(detail="비밀번호가 같지 않습니다", code="password_mismatch")
        
    def create(self, validated_data: Dict) -> Any:
        password = validated_data.pop("password")
        validated_data.pop("password2")
        
        user_save = super().create(password)
        user_save.set_password(password)
        user_save.save()
        
        return user_save


class LoginSerializer(serializers.ModelSerializer):
    error_messages: Dict[str, str] = {
        "login": "아이디와 비밀번호를 입력해주세요",
    }
    
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )
    
    class Meta:
        fields: List[str] = ["email", "password"]


    # def validate(self, data: Any) -> Dict[str, Any]:
    #     email: str = data.get("email")
    #     password: PasswordHasher = data.get("password")
        
    #     try:
    #         user = self.Meta.model.objects.get(email=email)
    #         user_password: PasswordHasher = user.password 
    #         pc: bool = PasswordHasher().verify(str(user_password).strip("argon2"), password)
    #         if pc:
    #             token: Any = RefreshToken.for_user(user)
    #             refresh = str(token)
    #             access = str(token.access_token)
    #             data: Dict[str, Any] = {
    #                 "msg": "로그인 성공",
    #                 "info": {
    #                     "email": user.email,
    #                     "refresh": refresh,
    #                     'access': access
    #                 }
    #             }
    #             return data
    #     except (self.Meta.model.DoesNotExist, VerifyMismatchError):
    #         raise ValidationError(self.error_messages)

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        email = data.get("email")
        password = data.get("password")
        
        try:
            user = self.Meta.model.objects.get(email=email)
            user_password = user.password 
            password_hasher = PasswordHasher()
            if password_hasher.verify(user_password, password):
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)
                data = {
                    "msg": "로그인 성공",
                    "info": {
                        "email": user.email,
                        "refresh": refresh,
                        'access': access
                    }
                }
                return data
        except AdminUser.DoesNotExist:
            raise ValidationError({"non_field_errors": ["유효하지 않은 사용자입니다."]})
        except VerifyMismatchError:
            raise ValidationError({"non_field_errors": ["비밀번호가 일치하지 않습니다."]})
        
        
        
class AdminRegisterSerializer(RegisterSerializer):  
    class Meta(RegisterSerializer.Meta):
        model = AdminUser  

        
class AdminLoginSerializer(LoginSerializer):  
    class Meta(LoginSerializer.Meta):
        model = AdminUser  
