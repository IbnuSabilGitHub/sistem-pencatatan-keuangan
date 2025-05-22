//  function untuk  handle open modal
function openModal(modalType) {
    const backdrop = document.getElementById("backdrop");
    // buat backdrop terlihat
    backdrop.classList.remove("invisible", "opacity-0");
    backdrop.classList.add("visible", "opacity-100");

    // pastikan semua modal tersembunyi dengan class hidden
    document.querySelectorAll(".modal").forEach((modal) => {
        modal.classList.add("hidden");
    });

    // Tampilkan modal yang sesuai
    document
        .querySelector(`.modal[data-modal="${modalType}"]`)
        .classList.remove("hidden");
}

// function untuk handle close modal
function closeModal() {
    const backdrop = document.getElementById("backdrop");
    backdrop.classList.remove("opacity-100");
    backdrop.classList.add("opacity-0");

    // Tunggu transisi selesai, baru sembunyikan dari interaksi
    setTimeout(() => {
        backdrop.classList.remove("visible");
        backdrop.classList.add("invisible");
    }, 300); // sama dengan duration-300
}


const tabs = document.querySelectorAll('[data-active]');
tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        tabs.forEach(b => b.setAttribute('data-active', 'false'));
        tab.setAttribute('data-active', 'true');
    });
});

document.querySelectorAll(".close-modal").forEach(btn => {
    btn.addEventListener("click", () => {
        closeModal();
    });
});