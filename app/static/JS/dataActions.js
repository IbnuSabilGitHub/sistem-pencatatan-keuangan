// Jika button add di klik, buka modal addNote

// Logika untuk menu actions
const menuButtons = document.querySelectorAll(".actions-menu-button"); // Ambil setiap tombol menu
const menuItems = document.querySelectorAll(".actions-menu"); // Ambil setiap item menu

menuButtons.forEach((menuButton) => {
    menuButton.addEventListener("click", function (event) {
        event.stopPropagation();
        const menu = menuButton.nextElementSibling;
        const isOpen = !menu.classList.contains("hidden");

        // Tutup semua menu
        menuItems.forEach((item) => {
            item.classList.add("hidden");
            item.previousElementSibling.setAttribute("aria-expanded", "false");
        });

        // Buka menu yang diklik
        if (!isOpen) {
            menu.classList.remove("hidden");
            menu.classList.add("block");
            menuButton.setAttribute("aria-expanded", "true");
        }
    });
});

document.addEventListener("click", function (event) {
    let clickedInsideAnyMenu = false;

    menuButtons.forEach((btn) => {
        const menu = btn.nextElementSibling;
        if (btn.contains(event.target) || menu.contains(event.target)) {
            clickedInsideAnyMenu = true;
        }
    });

    if (!clickedInsideAnyMenu) {
        menuItems.forEach((menu) => {
            menu.classList.add("hidden");
            menu.classList.remove("block");
            menu.previousElementSibling.setAttribute("aria-expanded", "false");
        });
    }
});

function hideMenu() {
    menuItems.forEach((menu) => {
        menu.classList.add("hidden");
        menu.classList.remove("block");
        menu.previousElementSibling.setAttribute("aria-expanded", "false");
    });
}

menuItems.forEach((menu) => {
    const actionList = menu.querySelectorAll("button");

    actionList.forEach((btn) => {
        const action = btn.dataset.action;

        if (action === "edit") {
            btn.addEventListener("click", function () {
                hideMenu();
                openModal('editNote');

            });
        } else if (action === "delete") {
            btn.addEventListener("click", function () {
                hideMenu();
                alert("Delete action triggered");
            });
        }
    });
});
document.getElementById('add-note').addEventListener('click', () => {
    openModal('addNote');
});
