// Contoh penggunaan jQuery untuk menampilkan gambar setelah tombol diklik
$(document).ready( () => { // Ketika dokumen sudah siap
    // Ambil elemen dengan id 'clickMe' dan tambahkan event click. Jika diklik Munculkan gambar dab hapus tombol
    $("#clickMe").click( () => { 
        // Ambil element dengan tag img dan hapus class hidden, tambahkan class block
        $("img").removeClass("hidden").addClass("block");
        // Ambil element dengan id clickMe dan hapus class block, tambahkan class hidden
        $("#clickMe").removeClass("block").addClass("hidden");
    });
});
