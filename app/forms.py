from django import forms
from .models import Food,orderedfoodbyuser,resetpassword
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import re
User=get_user_model()
class signupasuser(forms.Form):  
    username=forms.CharField( max_length=50, required=True, error_messages={'required': 'Username is required'},widget=forms.EmailInput(attrs={'class':'input'}))
    email=forms.EmailField( max_length=100, required=True, error_messages={'required': 'Email is required'},widget=forms.TextInput(attrs={'class':'input'}))
    password=forms.CharField( required=True, error_messages={'required': 'Password is required'},widget=forms.PasswordInput(attrs={'class':'input'}))
    address=forms.CharField( required=True, error_messages={'required': 'Address is required'},widget=forms.TextInput(attrs={'class':'input'}))
    phone=forms.CharField( required=True, error_messages={'required': 'Phone is required'},widget=forms.NumberInput(attrs={'class':'input'}))
    def clean_username(self):
        data = self.cleaned_data.get("username")
      
        if len(data)<4 or len(data)>20:
            raise forms.ValidationError("username must be between 4 to 20 length")
        if User.objects.filter(username=data):
            raise forms.ValidationError("Username is already taken")
        username_regex=r'^[a-zA-Z._-]{1,150}$'
        if not re.match(username_regex,data):
            raise forms.ValidationError("Username can only conatins .-_ symbol and Alphebet")

        return data
    def clean_email(self):
        data=self.cleaned_data.get("email")
        email_regex = (
            r'^[a-zA-Z0-9._%+-]+@'
            r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        )
        if not re.match(email_regex, data):
            raise forms.ValidationError('Enter a valid email address.')
        if User.objects.filter(email=data):
            raise forms.ValidationError("email is already taken")
        return data
    def clean_password(self):
        data=self.cleaned_data.get("password")
        if len(data)<7 :
            raise forms.ValidationError("Password mustbe of altleast 7 digits")
        return data
    def clean_phone(self):
        data=self.cleaned_data.get("phone")
        if len(data)!=10:
            raise forms.ValidationError("Phone number must be of 10 digit")
        return data
class sigupasresturant(forms.Form):
    username=forms.CharField( max_length=20, required=True, error_messages={'required': 'Username is required'})
    email=forms.CharField(  required=True, error_messages={'required': 'Email is required'})
    address=forms.CharField(  required=True, error_messages={'required': 'Address is required'})
    logititude=forms.CharField( required=True, error_messages={'required': 'logititude is required'})
    latitude=forms.CharField(  required=True, error_messages={'required': 'latitude is required'})
    phone=forms.CharField( max_length=10, required=True, error_messages={'required': 'Phone is required'})
    cpassword=forms.CharField(  required=True, error_messages={'required': 'confrim Password  is required'})
    password=forms.CharField(  required=True, error_messages={'required': 'Password  is required'})
    photo=forms.ImageField(required=True, error_messages={'required': 'photo  is required'})
    
    def clean_username(self):
        data=self.cleaned_data.get("username")
        if len(data)<3:
            raise forms.ValidationError("Username length must be greater than 3")
        if User.objects.filter(username=data):
            raise forms.ValidationError("Username is already taken")
        username_regex=r'^[a-zA-Z._-]{1,150}$'
        if not re.match(username_regex,data):
            raise forms.ValidationError("Username can only conatins .-_ symbol and Alphebet")

        return data
    def clean_email(self):
        data=self.cleaned_data.get("email")
        email_regex = (
            r'^[a-zA-Z0-9._%+-]+@'
            r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        )
        if not re.match(email_regex, data):
            raise forms.ValidationError('Enter a valid email address.')
        if User.objects.filter(email=data):
            raise forms.ValidationError("email is already taken")
        return data
    def clean_password(self):
        cpassword=self.get("password")
        data=self.cleaned_data.get("password")
        if len(data)<7:
            raise forms.ValidationError("password length must be greater than 7")
        if cpassword!=data:
            raise forms.ValidationError("password and confrim password is not same")
        return data
    def clean_phone(self):
        data=self.cleaned_data.get("phone")
        if len(data)!=10:
            raise forms.ValidationError("phone must be of 10 digits")
        if not data.startswith('98'):
              raise forms.ValidationError("Phone must start with 98")
        print(data)
        return data
        
   
class signupasdelivery(forms.Form):
    password=forms.CharField(max_length=20, required=True,error_messages={"required":"password is required"})
    username=forms.CharField(max_length=20, required=True,error_messages={"required":"Username is required"})
    email=forms.EmailField(required=True,error_messages={"required":"Email is required"})
    address=forms.CharField(required=True,error_messages={"required":"address field is required"})
    phone=forms.CharField(required=True,error_messages={"required":"phone is required"})
    photo=forms.ImageField(required=True,error_messages={"required":"photo is required"})
    cpassword=forms.CharField(max_length=20, required=True,error_messages={"required":"confrim password is required"})
    
    def clean_username(self):
        data=self.cleaned_data.get("username")
        if len(data)<3:
            raise forms.ValidationError("Username length must be greater than 3")
        if User.objects.filter(username=data):
            raise forms.ValidationError("Username is already taken")
        username_regex=r'^[a-zA-Z._-]{1,150}$'
        if not re.match(username_regex,data):
            raise forms.ValidationError("Username can only conatins .-_ symbol and Alphebet")

        return data
    def clean_password(self):
        data=self.cleaned_data.get("password")
        cpassword=self.get("password")
        if len(data)<7:
            raise forms.ValidationError("password length must be greater than 7")
        if cpassword!=data:
            raise forms.ValidationError("password and confirmpassword is not same")
        return data
    
    def clean_email(self):
        data=self.cleaned_data.get("email")
        email_regex = (
            r'^[a-zA-Z0-9._%+-]+@'
            r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        )
        if not re.match(email_regex, data):
            raise forms.ValidationError('Enter a valid email address.')
        if User.objects.filter(email=data):
            raise forms.ValidationError("email is already taken")
        return data
    def clean_phone(self):
        data=self.cleaned_data.get("phone")
        if len(data)!=10:
            raise forms.ValidationError("phone must be of 10 digits")
        return data
class loginvalidate(forms.Form):
    username=forms.CharField(required=True,error_messages={"required":"Username or email is required"},widget=forms.TextInput(attrs={'class':'input'}))
    password=forms.CharField(required=True,error_messages={"required":"Password is required"},widget=forms.PasswordInput(attrs={'class':'input'}))
    def clean_username(self):
        
        data=self.cleaned_data.get("username")
        if '@gmail.com' in data:
            user= User.objects.filter(email=data)
            if user.exists():
                data=user.first().username
            else:
                raise forms.ValidationError("Email or Password is wrong")
        else:
             if  not User.objects.filter(username=data).exists():
                  raise forms.ValidationError("Email or Password is wrong")
                 
                   


        return data
class validateorder(forms.Form):
    totalamount=forms.IntegerField(required=True,error_messages={"required":" total amount is required"})
    totalprice=forms.IntegerField(required=True,error_messages={"required":"total price is required"})
    address=forms.CharField(required=True,error_messages={"required":"address field is required"})
    def clean_totalamount(self):
        totalamount = self.cleaned_data.get('totalamount')
        food_id = self.data.get('foodid')
        if food_id:
            try:
                food_item = Food.objects.get(id=food_id)
                if totalamount > food_item.stock_level:
                    raise forms.ValidationError("Total amount exceeds available stock.")
                if not food_item.resturant_name.isopene:
                    raise forms.ValidationError("Sorry the resturant is closed")

            except Food.DoesNotExist:
                raise forms.ValidationError("Food item does not exist.")

        return totalamount
class validatedelivery(forms.Form):
    otp=forms.CharField(required=True,error_messages={"required":" Otp is required"})
    foodid=forms.IntegerField(required=True,error_messages={"required":"Invalid food pickup"})
    userid=forms.IntegerField(required=True,error_messages={"required":"Invalid user"})
    
    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        foodid = self.data.get('foodid')
        userid=self.data.get('userid')
        if foodid:
          try:
                food_item = orderedfoodbyuser.objects.get(id=foodid)
                if otp != food_item.otpfordeliveryman:
                    print(otp)
                    print(food_item.otpfordeliveryman)
                    raise forms.ValidationError("Otp does not matches")
                userinfo=User.objects.get(id=userid)
                if not userinfo. isdelivery:
                    raise forms.ValidationError("you are not allowed to pick order")
                

          except Food.DoesNotExist:
                raise forms.ValidationError("Food item does not exist.")
        return otp
class validatecustomer(forms.Form):
    otp=forms.CharField(required=True,error_messages={"required":" Otp is required"})
    foodid=forms.IntegerField(required=True,error_messages={"required":"Invalid food pickup"})
    userid=forms.IntegerField(required=True,error_messages={"required":"Invalid user"})
    
    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        foodid = self.data.get('foodid')
        userid=self.data.get('userid')
        if foodid:
          try:
                food_item = orderedfoodbyuser.objects.get(id=foodid)
                if otp != food_item.otpforuser:
                   
                    raise forms.ValidationError("Otp does not matches")
                userinfo=User.objects.get(id=userid)
                if not userinfo. isdelivery:
                    raise forms.ValidationError("you are not allowed to deliver order")
                

          except Food.DoesNotExist:
                raise forms.ValidationError("Food item does not exist.")
        return otp

        
    
    
class validateemail(forms.Form):
    email=forms.CharField(required=True,error_messages={"required":" email is required"})
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
               if not User.objects.filter(email=email).exists():
                 raise forms.ValidationError("email does not matches")
        except Food.DoesNotExist:
                raise forms.ValidationError("Food item does not exist.")
        return email
class validateresetpassword(forms.Form):
    email=forms.CharField(required=True,error_messages={"required":" email is required"})
    otp=forms.CharField(required=True,error_messages={"required":" otp is required"})
    password=forms.CharField(required=True,error_messages={"required":" password is required"})
    cpassword=forms.CharField(required=True,error_messages={"required":" confrim password is required"})
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
               if not resetpassword.objects.filter(resetuser__email=email).exists():
                 raise forms.ValidationError("email does not matches")
        except Food.DoesNotExist:
                raise forms.ValidationError("Food item does not exist.")
        return email
    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        email = self.cleaned_data.get('email')
        try:
               if not resetpassword.objects.filter(resetuser__email=email , otp=otp).exists():
                 raise forms.ValidationError("otp does not matches")
        except Food.DoesNotExist:
                raise forms.ValidationError("Food item does not exist.")
        return otp
    def clean_password(self):
        password=self.cleaned_data.get("password")
        cpassword=self.data.get("cpassword")
        print(password,cpassword)
        if len(password)<7:
            raise forms.ValidationError("password length must be greater than 7")
        if cpassword!=password:
            raise forms.ValidationError("password and confrim password is not matched")

        return password




    







    







