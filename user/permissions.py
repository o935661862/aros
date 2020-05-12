from rest_framework import permissions



class AdminPermission(permissions.BasePermission):


	def has_permission(self, request, view):

		if request.user.is_authenticated:
	
			if request.user.user_type_id == 1:
			
				return True
				
			else:
			
				return False
				
		else:
		
			return False



class IsSelfOrAdmin(permissions.BasePermission):


	def has_object_permission(self, request, view, obj):
		
		if request.user.is_authenticated:
		
			print('a')
		
			if request.user.user_type_id != 1:

				print('f')
				return obj == request.user
				
			else:
				
				print('t')

				return True				
		
		else:

			return False