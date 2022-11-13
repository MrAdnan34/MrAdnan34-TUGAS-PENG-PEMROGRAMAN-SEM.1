from docx import Document

document = Document()
text = document.add_paragraph('''TUGAS PERTEMUAN 12\n-> Membuat file docx dan diisi dengan biodata
\nNama : Muh. Adnan Putra Amiruddin
NIM : H071221080\nMenempuh pendidikan S-1 di : Universitas Hasanuddin
Fakultas : Matematika dan Ilmu Pengetahuan Alam (MIPA)\nProdi : Sistem Informasi
Umur : 18 tahun''')
document.save('Biodata.docx')