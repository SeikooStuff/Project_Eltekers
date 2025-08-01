import uuid
from django.db import models

class OrganisasiDaerah(models.Model):
    id_organisasi_daerah = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class PengurusDaerah(models.Model):
    id_pengurus_daerah = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_pengurus_daerah = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
#    organisasi_daerah = models.ForeignKey(OrganisasiDaerah, on_delete=models.CASCADE)

class PengurusSasana(models.Model):
#    id_sasana = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_pengurus_sasana = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_pengurus_sasana = models.CharField(max_length=255)
    no_telp_pengurus_sasana = models.CharField(max_length=20)

class Sasana(models.Model):
    id_sasana = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_sasana = models.CharField(max_length=255)
    sejak = models.IntegerField()
    alamat_sasana = models.TextField()
    provinsi = models.CharField(max_length=255)
    kota_kabupaten = models.CharField(max_length=255)   
    kecamatan = models.CharField(max_length=255)
    kelurahan = models.CharField(max_length=255)
    jumlah_instruktur = models.IntegerField()
    jumlah_peserta = models.IntegerField()
    peserta_aktif = models.IntegerField()
    jumlah_latihan_per_minggu = models.IntegerField()
    link_gmap = models.URLField(max_length=500, blank=True, null=True)
    profile = models.ImageField(upload_to='sasana_profiles/', blank=True, null=True)

    def __str__(self):
        return self.nama_sasana
#    pengurus_daerah = models.ForeignKey(PengurusDaerah, on_delete=models.CASCADE)
#    pengurus_sasana = models.OneToOneField(PengurusSasana, on_delete=models.CASCADE)

class JadwalLatihan(models.Model):
    id_jadwal = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tanggal_latihan = models.DateField()
    jam_latihan = models.TimeField()
#    sasana = models.ForeignKey(Sasana, on_delete=models.CASCADE)

class Instruktur(models.Model):
    id_instruktur = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_instruktur = models.CharField(max_length=255)
    sertifikasi = models.BooleanField()
    tanggal_sertifikasi = models.DateField()
    file_sertifikat = models.FileField()

    sasana = models.ForeignKey(Sasana, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama_instruktur

class Peserta(models.Model):
    id_peserta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_peserta = models.CharField(max_length=255)
    tanggal_lahir_peserta = models.DateField()
    kendala_terapi = models.TextField()

    sasana = models.ForeignKey(Sasana, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama_peserta

class Peraga(models.Model):
    id_peraga = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_peraga = models.CharField(max_length=255)
    #sasana = models.ForeignKey(Sasana, on_delete=models.CASCADE)

class Pelatihan(models.Model):
    id_pelatihan = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_pelatihan = models.CharField(max_length=255)
    tanggal_pelatihan = models.DateField()
    penyelenggara = models.CharField(max_length=255)
    deskripsi = models.TextField()
#    instruktur = models.ManyToManyField(Instruktur)

class Gerakan(models.Model):
    id_gerakan = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_gerakan = models.CharField(max_length=255)
    deskripsi_acuan = models.TextField()
    referensi_gerakan = models.TextField()
#    peraga = models.ManyToManyField(Peraga)

class Evaluasi(models.Model):
#    id_evaluasi = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    peserta = models.ForeignKey(Sasana, on_delete=models.CASCADE)
#    gerakan = models.ForeignKey(Sasana, on_delete=models.CASCADE)
    tanggal_evaluasi = models.DateField()
    periode_evaluasi = models.DateField()
    hasil_evaluasi = models.TextField()


# API
class Provinsi(models.Model):
    id = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Kabupaten(models.Model):
    id = models.IntegerField(primary_key=True)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama
    
class Kecamatan(models.Model):
    id = models.IntegerField(Kabupaten, primary_key=True)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Kelurahan(models.Model):
    id = models.IntegerField(primary_key=True)
    provinsi = models.ForeignKey(Kecamatan, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama