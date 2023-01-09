from django.shortcuts import render
from pickle import load
from .models import Emp_data  

model = load(open('./savedModels/attr_model.pkl','rb'))

# Create your views here.
def root(request):
    table = Emp_data.objects.all()
    if request.method == 'POST':
        EmpNum = request.POST['EmployeeNumber']
        data = Emp_data.objects.filter(EmployeeNumber = EmpNum).values()[0]
        Edept = {'Human Resource':0,'Research & Development':1,'Sales':2}
        Eedufield = {'Human Resource':0,'Life Sciences':1,'Marketing':2,'Medical':3,'Other':4,'Technical':5}        
        EGender = {'Male':1,'Female':0}
        Ejobrole = {'Healthcare Representative':0,'Human Resources':1,'Laboratory Technician':2,'Manager':3,'Manufacturing Director':4,'Research Director':5,'Research Scientist':6,'Sales Executive':7,'Sales Representative':8}

        data['Department'] = Edept[data['Department']]
        data['EducationField'] = Eedufield[data['EducationField']]
        data['Gender'] = EGender[data['Gender']]
        data['JobRole'] = Ejobrole[data['JobRole']]
        del data['id']
        li = []
        for i in data.values():
            li.append(i)
        ypred = model.predict([li])
        if (ypred == 0):
            op = 'Low Risk of Attrition'
        else:
            op = 'High Risk of Attrition'
        return render(request, 'main.html', {'result':op, 'qres':table})
    return render(request, 'main.html',{'qres':table}) 
