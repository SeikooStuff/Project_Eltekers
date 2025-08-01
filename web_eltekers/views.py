from django.shortcuts import get_object_or_404, render, redirect
from .forms import SasanaForm, PesertaForm, InstrukturForm
from .models import Sasana, Instruktur, Peserta

# Sasana
def create_sasana(request):
    if request.method == 'POST':
        form = SasanaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-sasana')
    else:
        form = SasanaForm()
    return render(request, 'sasana_form.html', {'form': form})

def list_sasana(request):
    data = Sasana.objects.all()
    return render(request, 'sasana_list.html', {'data': data})

# Di sini, 'id_sasana' harus cocok dengan nama parameter di urls.py
def detail_sasana(request, id_sasana):
    sasana = get_object_or_404(Sasana, id_sasana=id_sasana)
    return render(request, 'sasana_detail.html', {'sasana': sasana})

def update_sasana(request, id_sasana):
    sasana = get_object_or_404(Sasana, id_sasana=id_sasana)
    if request.method == 'POST':
        form = SasanaForm(request.POST, request.FILES, instance=sasana)
        if form.is_valid():
            form.save()
            return redirect('list-sasana')
    else:
        form = SasanaForm(instance=sasana)
    return render(request, 'sasana_form.html', {'form': form})

def delete_sasana(request, id_sasana):
    sasana = get_object_or_404(Sasana, id_sasana=id_sasana)
    if request.method == 'POST':
        sasana.delete()
        return redirect('list-sasana')
    return render(request, 'sasana_confirm_delete.html', {'sasana': sasana})


# Peserta
def create_peserta(request, sasana_id):
#    sasana_id = request.GET.get('sasana_id')
    sasana = get_object_or_404(Sasana, id_sasana=sasana_id)

    if request.method == 'POST':
        form = PesertaForm(request.POST)
        if form.is_valid():
            peserta = form.save(commit=False)
            peserta.sasana = sasana
            peserta.save()
            return redirect('list-peserta', sasana_id=sasana.id_sasana)
    else:
        form = PesertaForm()

    return render(request, 'peserta_form.html', {'form': form, 'sasana': sasana})

# List Peserta
def list_peserta(request, sasana_id):
    sasana = get_object_or_404(Sasana, id_sasana=sasana_id)
    data = Peserta.objects.filter(sasana=sasana)
    return render(request, 'peserta_list.html', {'data': data, 'sasana': sasana})

# Detail Peserta
def detail_peserta(request, id_peserta):
    peserta = get_object_or_404(Peserta, id_peserta=id_peserta)
    return render(request, 'peserta_detail.html', {'peserta': peserta})

# Edit Peserta
def update_peserta(request, id_peserta):
    peserta = get_object_or_404(Peserta, id_peserta=id_peserta)
    sasana = peserta.sasana

    if request.method == 'POST':
        form = PesertaForm(request.POST, instance=peserta)
        if form.is_valid():
            form.save()
            return redirect('list-peserta', sasana_id=sasana.id_sasana)
    else:
        form = PesertaForm(instance=peserta)
    return render(request, 'peserta_form.html', {'form': form, 'sasana': sasana, 'peserta': peserta})

# Delete Peserta
def delete_peserta(request, id_peserta):
    peserta = get_object_or_404(Peserta, id_peserta=id_peserta)
    if request.method == 'POST':
        peserta.delete()
        return redirect('list-peserta')
    return render(request, 'peserta_confirm_delete.html', {'peserta': peserta})


# Instruktur
def create_instruktur(request, sasana_id):
#    sasana_id = request.GET.get('sasana_id')
    sasana = get_object_or_404(Sasana, id_sasana=sasana_id)

    if request.method == 'POST':
        form = InstrukturForm(request.POST, request.FILES)  
        if form.is_valid():
            instruktur = form.save(commit=False)
            instruktur.sasana = sasana
            instruktur.save()
            return redirect('list-instruktur', sasana_id=sasana.id_sasana)
    else:
        form = InstrukturForm()

    return render(request, 'instruktur_form.html', {'form': form, 'sasana': sasana})

# List Instruktur
def list_instruktur(request, sasana_id):
    sasana = get_object_or_404(Sasana, id_sasana=sasana_id)
    data = Instruktur.objects.filter(sasana=sasana)
    return render(request, 'instruktur_list.html', {'data': data, 'sasana': sasana})

# Detail Instruktur
def detail_instruktur(request, id_instruktur):
    instruktur = get_object_or_404(Instruktur, id_instruktur=id_instruktur)
    return render(request, 'instruktur_detail.html', {'instruktur': instruktur})

# Edit Instruktur
def update_instruktur(request, id_instruktur):
    instruktur = get_object_or_404(Instruktur, id_instruktur=id_instruktur)
    sasana = instruktur.sasana

    if request.method == 'POST':
        form = InstrukturForm(request.POST, request.FILES, instance=instruktur)
        if form.is_valid():
            form.save()
            return redirect('list-instruktur', sasana_id=sasana.id_sasana)
    else:
        form = InstrukturForm(instance=instruktur)
    return render(request, 'instruktur_form.html', {'form': form, 'sasana': sasana, 'instruktur':instruktur})

# Delete Instruktur
def delete_instruktur(request, id_instruktur):
    instruktur = get_object_or_404(Instruktur, id_instruktur=id_instruktur)
    if request.method == 'POST':
        instruktur.delete()
        return redirect('list-instruktur')
    return render(request, 'instruktur_confirm_delete.html', {'instruktur': instruktur})