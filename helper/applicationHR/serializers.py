from rest_framework import serializers


from helper.applicationHR.models import User, Summary #Users

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('id', 'name', 'positionId', 'age', 'salary', 'workedFor', 'recieved', 'scoreBefore', 'scoreAfter', 'starred' )



# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['name_company', 'username', 'phone', 'password', 'password2' ]
#         extra_kwargs = {
#             'password2': {'write_only': True}
#         }
#         def save(self):
#             user = User(
#                 phone=self.validated_data['phone'],
#                 username=self.validated_data['username'],
#                 name_company=self.validated_data['name_company'],
#             )
#             password = self.validated_data['password']
#             password2 = self.validated_data['password2']
#             if password != password2:
#                  raise serializers.ValidationError({'password': "Password most match"})
#             user.set_password(password)
#             user.save()
#             return user
class RegistrationSerializer(serializers.ModelSerializer):

	password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['username','name_company', 'phone', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}

	def	save(self):

		account = User(
					name_company=self.validated_data['name_company'],
					phone=self.validated_data['phone'],
					username=self.validated_data['username'],

				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.save()
		return account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['phone', 'username', 'position', 'assigments', 'last_login', 'date_joined', 'photo']
























'''class UsersSerializer(serializers.ModelSerializer):
    empl_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    class Meta:
        #model = Users
        #fields = ('name', 'employee_id')
        fields = '__all__'

'''