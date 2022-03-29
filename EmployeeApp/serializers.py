from rest_framework import serializers
from EmployeeApp.models import Department , Employee


class DepartmentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Department
        fields = (
            'id' ,
            'DepartmentName' 
        )

class EmployeeSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Employee
        fields = (
            'id' ,
            'EmployeeName' ,
            'Department' ,
            'DateOfJoining' ,
            'PhotoFileName'
        )