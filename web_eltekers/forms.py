from django import forms
from .models import Sasana, Peserta, Instruktur

class SasanaForm(forms.ModelForm):
    class Meta:
        model = Sasana
        fields = '__all__'
        widgets = {
            'nama_sasana': forms.TextInput(attrs={'class': 'form-control'}),
            'sejak': forms.NumberInput(attrs={'class': 'form-control'}),
            'alamat_sasana': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'kelurahan': forms.TextInput(attrs={'class': 'form-control'}),
            'kecamatan': forms.TextInput(attrs={'class': 'form-control'}),
            'kota_kabupaten': forms.TextInput(attrs={'class': 'form-control'}),
            'provinsi': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_ketua': forms.TextInput(attrs={'class': 'form-control'}),
            'no_wa_ketua': forms.NumberInput(attrs={'class': 'form-control'}),
            'nama_pengurus': forms.TextInput(attrs={'class': 'form-control'}),
            'no_wa_pengurus': forms.NumberInput(attrs={'class': 'form-control'}),
            'jumlah_instruktur': forms.NumberInput(attrs={'class': 'form-control'}),
            'jumlah_peserta': forms.NumberInput(attrs={'class': 'form-control'}),
            'peserta_aktif': forms.NumberInput(attrs={'class': 'form-control'}),
            'jumlah_latihan_per_minggu': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PesertaForm(forms.ModelForm):
    class Meta:
        model = Peserta
        fields = '__all__'
        widgets = {
            'nama_peserta': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_lahir_peserta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'kendala_terapi': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sasana': forms.Select(attrs={'class': 'form-control'}),
        }

class InstrukturForm(forms.ModelForm):
    class Meta:
        model = Instruktur
        fields = '__all__'
        widgets = {
            'nama_instruktur': forms.TextInput(attrs={'class': 'form-control'}),
            'sertifikasi': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tanggal_sertifikasi': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'file_sertifikat': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'sasana': forms.Select(attrs={'class': 'form-control'}),
        }