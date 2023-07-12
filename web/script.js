// Variáveis
var mpM = document.getElementById("mpM");
var mpP = document.getElementById("mpP");
var mpC = document.getElementById("mpC");
var mpI = document.getElementById("mpI");
var mpR = document.getElementById("mpR");
var mpE = document.getElementById("mpE");
var mpL = document.getElementById("mpL");

// Botões
window.addEventListener("load", function() {
    //Botões do gerador
    document.getElementById ("btnNormal").addEventListener ("click", normal);
    document.getElementById ("btnBoss").addEventListener ("click", boss);
    document.getElementById ("btnMP").addEventListener ("click", mapaPerg);
    document.getElementById ("btnBFight").addEventListener ("click", bossFight);
})

// Botão de drop normal
function normal() {
    limpaTela();
    eel.dropMenu(1, 0);
}

// Botão de drop de boss
function boss() {
    limpaTela();
    eel.dropMenu(2, 0);
}

// Botão de drop normal

// Início das funções de botões magia de pergaminho
function mapaPerg() {
    limpaTela();
    if ((mpM.checked) && (mpI.checked)) eel.dropMenu(3, 2);

    else if ((mpM.checked) && (mpR.checked)) eel.dropMenu(3, 3);

    else if ((mpM.checked) && (mpE.checked)) eel.dropMenu(3, 4);

    else if ((mpM.checked) && (mpL.checked)) eel.dropMenu(3, 5);

    else if ((mpP.checked) && (mpC.checked)) eel.dropMenu(4, 1);

    else if ((mpP.checked) && (mpI.checked)) eel.dropMenu(4, 2);

    else if ((mpP.checked) && (mpR.checked)) eel.dropMenu(4, 3);

    else if ((mpP.checked) && (mpE.checked)) eel.dropMenu(4, 4);

    else if ((mpP.checked) && (mpL.checked)) eel.dropMenu(4, 5);
}

// Botão drop de mapa
function bossFight() {
    limpaTela();
    if (b1.checked) eel.dropMenu(5, 1);

    else if (b2.checked) eel.dropMenu(5, 2);

    else if (b3.checked) eel.dropMenu(5, 3);
}

// Imprimir na tela
eel.expose(printDrop);
function printDrop(item) {
    let display = document.getElementById("display");
    display.insertAdjacentHTML("beforeend", ("<p>"+item));
}

// Limpar a tela
eel.expose(limpaTela);
function limpaTela() {
    let display = document.getElementById("display");
    display.innerHTML = "";
}

// Desmarcar checkbox
function desmarcarCheck(cId) {
    if (cId == "mpM" || cId == "mpP") {
        if (cId != "mpM") mpM.checked = false;

        if (cId != "mpP") {
            mpP.checked = false;
            mpC.checked = false;
        }
    }
    
    if (cId == "mpC" || cId == "mpI" || cId == "mpR" || cId == "mpE" || cId == "mpL") {
        if (cId != "mpC") mpC.checked = false;

        if (cId != "mpI") mpI.checked = false;

        if (cId != "mpR") mpR.checked = false;

        if (cId != "mpE") mpE.checked = false;

        if (cId != "mpL") mpL.checked = false;

        if (mpC.checked) {
            mpM.checked = false;
            mpP.checked = true;
        }
    }

    if (cId == "b1" || cId == "b2" || cId == "b3") {
        if (cId != "b1") b1.checked = false;

        if (cId != "b2") b2.checked = false;

        if (cId != "b3") b3.checked = false;
    }
}