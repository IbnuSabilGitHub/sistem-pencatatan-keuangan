$('#loadData').click(() => { // Ketika tombol dengan id loadData diklik
    $.get('/api/data', (response) => { // Mengambil data dari server menggunakan metode GET
        const message = response.message; // Mengambil pesan dari respons
        $('#output').text(message); // Menampilkan pesan di elemen dengan id output
    }
    ).fail(() => { // Jika terjadi kesalahan saat mengambil data
        $('#output').text('Error loading data'); // Menampilkan pesan kesalahan
    });
});
