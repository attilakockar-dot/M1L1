
function saatiGuncelle() {
    const saatKutusu = document.getElementById("saat");
    if (!saatKutusu) return;

    const simdi = new Date();
    const istanbulSaat = simdi.toLocaleTimeString("tr-TR", {
        timeZone: "Europe/Istanbul"
    });

    saatKutusu.textContent = istanbulSaat;
}

saatiGuncelle();
setInterval(saatiGuncelle, 1000);
