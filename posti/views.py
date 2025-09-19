from django.shortcuts import render,redirect
from .forms import MyForm, LoginForm
from .models import *
from .librerie.library import main,toCammelCase
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
# Create your views here.
from .librerie.library1 import generaPosti,transform,cognomi


def generatoreDiPosti(input):
    input, k =transform(input)
    if k==0:
        results=generaPosti(input)
    else:
        results=input
    return results,k


# @login_required
# def changePosti(request):
#     k=0
#     results = None
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         inputs=[]
#         if form.is_valid():
#             for i in range(21):
#                 inputs.append(form.cleaned_data[f'posto{i+1}'].upper()) #creo l'array con i nomi in input per la prima configurazione dei posti
#             results,k = generatoreDiPosti(inputs)
#             if k==0:
#                 mapped_results = {f'posto{i+1}': results[i] for i in range(21)}
#                 ModelloPosti.objects.create(**mapped_results)

#     else:
#         form = MyForm()
#     print(results)
#     return render(request, 'posti/changePosti.html', {'form': form, 'results': results, 'error':k})


@login_required
def cambiaPosti_view(request):  #permette di modificare i posti dopo che sono stati creati nel database (l'ultimo di essi)
    obj=ModelloPosti.objects.last()
    if request.method=='POST':
        form=MyForm(request.POST, instance=obj)
        if form.is_valid():
            action = request.POST.get('action')
            if action == 'Conferma':
                inputs=[]
                for i in range(len(cognomi)):
                    inputs.append(form.cleaned_data[f'posto{i+1}'].upper())
                results, k=transform(inputs)
                print(inputs)
                print(results)
                if k==0:
                    inputs=toCammelCase(inputs)
                    for i in range(len(cognomi)):
                        setattr(obj, f'posto{i+1}', inputs[i])
                    obj.save() 
                    return redirect(request.path)
                else:
                    return render(request, 'posti/cambiaPosti.html', {'form':form, 'results':results})
                
            elif action == 'GeneraPosti':
                inputs=[]
                for i in range(len(cognomi)):
                    inputs.append(form.cleaned_data[f'posto{i+1}'].upper())
                print(inputs)
                results, k=generatoreDiPosti(inputs)
                print(results)
                if k==0:
                    results=toCammelCase(results) #fai si che i posti siano title

                    inputs=toCammelCase(inputs) # fa si che se cambi due persone anche la vecchia disposizione viene aggiornata
                    for i in range(len(cognomi)):
                        setattr(obj, f'posto{i+1}', inputs[i])
                    obj.save() 

                    for i in range(len(cognomi)):
                        setattr(obj, f'posto{i+1}', results[i])  # crea un oggetto  
                    ModelloPosti.objects.create(posto1=results[0],
                                                posto2=results[1],
                                                posto3=results[2],
                                                posto4=results[3],
                                                posto5=results[4],
                                                posto6=results[5],
                                                posto7=results[6],
                                                posto8=results[7],
                                                posto9=results[8],
                                                posto10=results[9],
                                                posto11=results[10],
                                                posto12=results[11],
                                                posto13=results[12],
                                                posto14=results[13],
                                                posto15=results[14],
                                                posto16=results[15],
                                                posto17=results[16],
                                                posto18=results[17],
                                                posto19=results[18],
                                                posto20=results[19],
                                                posto21=results[20],
                                                posto22=results[21] ) 
                    return redirect(request.path)
                else:
                    return render(request, 'posti/cambiaPosti.html', {'form':form, 'results':results})
            else:
                obj.delete()
                return redirect(request.path)

    else:
        form=MyForm(instance=obj)

    return render(request, 'posti/cambiaPosti.html', {'form':form})




def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('cambia_posti')
            else:
                print("invalid")
                messages.error(request, "Username or password is incorrect.")

    else:
        form=LoginForm()
    return render(request,'LogInView/login.html',{'form': form})


def posti(request):
    obj=ModelloPosti.objects.last()
    posti=convertPostiToArray(obj)
    return render(request,'NotLoggedInView/posti.html',{'posti':posti,'date':obj.data})


def logout_view(request):
    logout(request)
    return redirect('posti')


def convertPostiToArray(obj):
    posti=[]
    posti.append(obj.posto1)
    posti.append(obj.posto2)
    posti.append(obj.posto3)
    posti.append(obj.posto4)
    posti.append(obj.posto5)
    posti.append(obj.posto6)
    posti.append(obj.posto7)
    posti.append(obj.posto8)
    posti.append(obj.posto9)
    posti.append(obj.posto10)
    posti.append(obj.posto11)
    posti.append(obj.posto12)
    posti.append(obj.posto13)
    posti.append(obj.posto14)
    posti.append(obj.posto15)
    posti.append(obj.posto16)
    posti.append(obj.posto17)
    posti.append(obj.posto18)
    posti.append(obj.posto19)
    posti.append(obj.posto20)
    posti.append(obj.posto21)
    posti.append(obj.posto22)
    return posti
    