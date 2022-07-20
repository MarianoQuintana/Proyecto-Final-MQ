from django.shortcuts import render
from emp.models import Empresa, Empleados, Clientes
from emp.forms import EmpresaFormulario, EmpleadosFormulario, ClientesFormulario

def ver_empresa(request):
    context={}
    context["empresa"] = Empresa.objects.all()
    return render(request,'emp/mostrar_empresa.html', context)


def ver_empleados(request):
    context={}
    context["empleados"] = Empleados.objects.all()
    
    return render(request,'emp/mostrar_empleados.html', context)    

def ver_clientes(request):
    context={}
    context["clientes"] = Clientes.objects.all()
   
    return render(request,'emp/mostrar_clientes.html', context)


def empresaFormulario(request):
    if request.method == 'POST':
        aformulario = EmpresaFormulario(request.POST)
        print(aformulario)
        if aformulario.is_valid:
            informacion = aformulario.cleaned_data
            empresa = Empresa(nombre =informacion["nombre"], cuit = informacion["cuit"])
            empresa.save() 

            return render(request,'emp/empresa.html',{})    
    else:
         aformulario = EmpresaFormulario()

         return render(request,'emp/empresa.html',{"aformulario": aformulario})


def empleadosFormulario(request):
    if request.method == 'POST':
        bformulario = EmpleadosFormulario(request.POST)
        print(bformulario)
        if bformulario.is_valid:
            informacion = bformilario.cleaned_data
            empleados= Empleados(nombre =informacion["nombre"], edad = informacion["edad"], tel = informacion["tel"], mail = informacion["mail"],)
            empleados.save() 

            return render(request,'emp/empleados.html',{})    
    else:
         bformulario = EmpleadosFormulario()

         return render(request,'emp/empleados.html',{"bformulario": bformulario})

        

def clientesFormulario(request):
    if request.method == 'POST':
        cformulario = ClientesFormulario(request.POST)
        print(cformulario)
        if cformulario.is_valid:
            informacion = cformulario.cleaned_data
            clientes = Clientes(nombre =informacion["nombre"], edad = informacion["edad"], tel = informacion["tel"], mail = informacion["mail"],)
            clientes.save() 

            return render(request,'emp/clientes.html',{})    
    else:
         cformulario = ClientesFormulario()

         return render(request,'emp/clientes.html',{"cformulario": cformulario})
      
