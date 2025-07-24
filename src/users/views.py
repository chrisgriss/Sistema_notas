from django.shortcuts import render, redirect
import requests

path_ = 'http://127.0.0.1:5000/api'

def login(request):
    global path_
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'users/login.html', {"message" : "Faltan credenciales"})
        
        try:
            response = requests.post(f'{path_}/login', json={
                "username" : username, 
                "password" : password} )
            if response.status_code == 200:
                return redirect('home')
            elif response.status_code == 401:
                message = response.json().get('message',f'Contraseña incorrecta')
            elif response.status_code == 404:
                message = response.json().get('message',f'Usuario no encontrado')
        except requests.RequestException as e:
            print("error en exeption" + e)
        return render(request, 'users/login.html', {"message" : message})
    return render(request, 'users/login.html')

def signin(request):
    global path_
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        correo = request.POST.get('email')
        asignatura = request.POST.get('asignatura')
        if not username or not password or not name or not correo or not asignatura:
            return render(request, 'users/signin.html', {"message" : "Faltan credenciales"})
        try:
            response = requests.post(f'{path_}/signin', json={
                "username" : username, 
                "name" : name,
                "password" : password,
                "email" : correo,
                "asignatura" : asignatura} )
            if response.status_code == 201:
                return redirect('login')
            elif response.status_code == 401:
                message = response.json().get('message','')
            elif response.status_code == 400:
                message = response.json().get('message','')
        except requests.RequestException as e:
            print("error en exeption" + e)
        return render(request, 'users/signin.html', {"message" : message})
    return render(request, 'users/signin.html')

def logout(request):
    global path_
    try:
        response = requests.delete(f'{path_}/logout')
        if response.status_code == 200:
            return redirect('login')
    except requests.RequestException as e:
        pass
    return redirect(request, 'users/login.html')
