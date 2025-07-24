from django.shortcuts import render
import requests

path_ = 'http://127.0.0.1:5000/api'

def home(request):
    global path_
    asignatura = ''
    mensaje = ''
    try:
        response = requests.get(f'{path_}/home')
        if response.status_code == 200:
            data = response.json()
            asignatura = data.get('asignatura','')
            mensaje = data.get('message','')
        elif response.status_code == 401:
            data = response.json()
            mensaje = data.get('error','')
    except requests.RequestException as e:
        pass
    return render(request, 'note_log/home.html', {'mensaje' : mensaje, 'asignatura' : asignatura})

def ver_notas(request):
    global path_
    notas = []
    promedio = 0.0
    try:
        response = requests.get(f'{path_}/mostrar_notas')
        if response.status_code == 200:
            data = response.json()
            notas = data.get('notas',[])
            promedio = float(data.get('promedio', 0.0))
    except requests.RequestException as e:
        pass

    return render(request, 'note_log/ver_notas.html', {'notas' : notas, 'promedio' : promedio})

def registro(request):
    global path_
    if request.method == 'POST':
        nota_str = request.POST.get('nota')
        message = ''
        if not nota_str:
            return render(request, 'note_log/registro_notas.html', {"message": "Faltan credenciales"})
        
        try:
            nota = int(nota_str)
            response = requests.post(f'{path_}/registro', json={"nota": nota})

            if response.status_code == 200:
                data = response.json()
                message = data.get('message', 'Nota Subida Exitosamente')
            elif response.status_code == 400:
                data = response.json()
                message = data.get('message','Nota no válida')
        except requests.RequestException as e:
            print("Error en exception" + e)
        return render(request, 'note_log/registro_notas.html', {'message':message})
    return render(request, 'note_log/registro_notas.html')