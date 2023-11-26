<a name="atas"></a>

## Helpful Links

[SPESIFIKASI](https://docs.google.com/document/d/1W5QSSHVrXvArj3Aonw4FhbfctBK6J2YGefXpWsLW43Y/edit)

[Laporan](https://docs.google.com/document/d/1BonNAbPqu24nlL_vFE1AMAtcJSWL3UMr4pcaxNmZq5c/edit#heading=h.z5pmwbivcb0h)

## Tentang Aplikasi

<div align="center">
    <h2>HTML Checker</h2>
    <p>By Kelompok JIMMY 88</p>
    <br/>
    <br/>
</div>


HTML (Hypertext Markup Language) adalah bahasa markup yang digunakan untuk membuat struktur dan tampilan konten web. HTML adalah salah satu bahasa utama yang digunakan dalam pengembangan web dan digunakan untuk menggambarkan bagaimana elemen-elemen konten, seperti teks, gambar, tautan, dan media, akan ditampilkan di browser web. Setiap dokumen HTML dimulai dengan elemen `<html>`, lalu diikuti dengan `<head>` (untuk metadata dan tautan ke file eksternal) dan `<body>` (untuk konten yang akan ditampilkan)
HTML menggunakan elemen-elemen (tags) untuk mengelompokkan dan mengatur konten. Contohnya, `<p>` digunakan untuk paragraf teks, `<h1>` hingga `<h6>` digunakan untuk judul, `<a>` untuk tautan, `<img>` untuk gambar, dan sebagainya. Elemen HTML sering memiliki atribut yang memberikan informasi tambahan tentang elemen tersebut. Contohnya adalah atribut src untuk gambar, href untuk tautan, dan class untuk memberikan elemen kelas CSS.
Sama seperti bahasa pada umumnya, HTML juga memiliki sintaks tersendiri dalam penulisannya yang dapat menimbulkan error jika tidak dipenuhi. Meskipun web browser modern seperti Chrome dan Firefox cenderung tidak menghiraukan error pada HTML memastikan bahwa HTML benar dan terbentuk dengan baik masih penting untuk beberapa alasan seperti Search Engine Optimization (SEO), aksesibilitas, maintenance yang lebih baik, kecepatan render, dan profesionalisme. 
Dibutuhkan sebuah program pendeteksi error untuk HTML. Oleh sebab itu, implementasikan sebuah program yang dapat memeriksa kebenaran HTML dari segi nama tag yang digunakan serta attribute yang dimilikinya. Pada tugas pemrograman ini, gunakanlah konsep Pushdown Automata (PDA) dalam mencapai hal tersebut yang diimplementasikan dalam bahasa Python. 

<p align="right">(<a href="#atas">kembali</a>)</p>

## Cara Kompilasi Program
Pertama-tama Clone repository terlebih dahulu
```
git clone https://github.com/Benardo07/Tubes-TBFO.git
```
Setelah berhasil di clone , buka folder hasil clone dalam vscode.
Pastikan anda berapa di root program 
Untuk menjalankan program , anda dapat menginput sesuai dengan format di bawah ini

```shell
python main.py pda.txt "nama_file_html_yang_ingin_dicek"
```
Note ** : pastikan file html berada di root yang sama dengan main.py


## Anggota Kelompok
| NIM |Nama |
|-----|-----|
|13522016|Zachary Samuel T|
|13522019|Wilson Yusda|
|13522055|Benardo|

<p align="right">(<a href="#atas">kembali</a>)</p>

## Pembagian Kerja
| NIM |Nama |Pembagian Kerja|
|-----|-----|
|13522016|Zachary Samuel T|membantu membuat PDA transition|
|13522019|Wilson Yusda|Laporan, membantu membuat PDA transition, Diagram PDA, states.py (pencocok initial dan final state)|
|13522055|Benardo|PDA , parser html , parser PDA ke struktur data dictionary, merancang seluruh transition function pada PDA, laporan|

<p align="right">(<a href="#atas">kembali</a>)</p>
