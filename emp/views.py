from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from emp.models import Empresa, Empleados, Clientes
from emp.forms import EmpresaFormulario, EmpleadosFormulario, ClientesFormulario, Busqueda_Clientes

def index(request):
    return render(request, 'emp/index.html',{})


def empresaFormulario(request):
    if request.method == 'POST':
        aformulario = EmpresaFormulario(request.POST)
       
        if aformulario.is_valid:
            informacion = aformulario.cleaned_data
            empresa= Empresa(nombre =informacion["nombre"], cuit = informacion["cuit"])
            empresa.save() 

            return render(request,'emp/empresa.html',{})   
    else:
         aformulario = EmpresaFormulario()


         return render(request,'emp/empresa.html',{"aformulario": aformulario})



def ver_empresa(request):
    context = {"empresa": Empresa.objects.all()}
       
    return render(request,'emp/mostrar_empresa.html', context)




def empleadosFormulario(request):
    if request.method == 'POST':
        bformulario = EmpleadosFormulario(request.POST)
        print(bformulario)
        if bformulario.is_valid:
            informacion = bformilario.cleaned_data
            empleados= Empleados(nombre =informacion["nombre"], edad = informacion["edad"], tel = informacion["tel"], mail = informacion["mail"],)
            empleados.save() 

            return redirect(reverse_lazy(request,'emp/empleados.html',{}))    
    else:
         bformulario = EmpleadosFormulario()

         return render(request,'emp/empleados.html',{"bformulario": bformulario})

def ver_empleados(request):
    context = {"empleados": Empleados.objects.all()}
       
    return render(request,'emp/mostrar_empleados.html', context)
   

        
def clientesFormulario(request):
    if request.method == 'POST':
        cformulario = ClientesFormulario(request.POST)
        print(cformulario)
        if cformulario.is_valid:
            informacion = cformulario.cleaned_data
            clientes = Clientes(nombre =informacion["nombre"], edad = informacion["edad"], tel = informacion["tel"], mail = informacion["mail"],)
            clientes.save() 

            return redirect(reverse_lazy(request,'emp/clientes.html',{}))    
    else:
         cformulario = ClientesFormulario()

         return render(request,'emp/clientes.html',{"cformulario": cformulario})

def ver_clientes(request):
    context = {"clientes": Clientes.objects.all()}
       
    return render(request,'emp/mostrar_clientes.html', context)



def buscarClientes(request):
    
    formulario_busqueda = Busqueda_Clientes()
    
    if request.GET:
        formulario_busqueda = Busqueda_Clientes(request.GET)
        if formulario_busqueda.is_valid():
            clientes = Clientes.objects.filter(nombre=formulario_busqueda.cleaned_data["criterio"]).all()
            return render(request,"app/busqueda_clientes.html", {"clientes": clientes})
    
    return render(request,"app/busqueda_clientes.html", {"formulario_busqueda":formulario_busqueda})      
