function fecharModal() {
    const modalResultado = document.getElementById("modalResultado");
    const modalErro = document.getElementById("modalErro");

    if (modalResultado) {
        modalResultado.style.display = "none";
    }

    if (modalErro) {
        modalErro.style.display = "none";
    }
}

document.addEventListener("keydown", function (evento) {
    if (evento.key === "Escape") {
        fecharModal();
    }
});

document.querySelectorAll(".modal").forEach(function (modal) {
    modal.addEventListener("click", function (evento) {
        if (evento.target === modal) {
            fecharModal();
        }
    });
});