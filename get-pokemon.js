function reset() { 
    if (typeof boxNumber === 'undefined') {
            boxNumber = "1";
    }
    box = document.getElementById("box");
    boxList = pokemonList[boxNumber];

    for (var i = 0; i < box.rows.length; i++) {
        for (var j = 0; j < box.rows[i].cells.length; j++) {
            let cell = box.rows[i].cells[j];
            let boxIndex = (i*6) + j;
            if (boxIndex < boxList.length) {
                let pokemon = boxList[boxIndex];
                let img = document.createElement("img");
                img.src = pokemon['image'];
                img.title = pokemon['number'] + '. ' + pokemon['name'];
                img.height = 100;
                img.width = 100;
                if (cell.hasChildNodes()) {
                    cell.replaceChild(img, cell.childNodes[0]);
                } else {
                    cell.appendChild(img);
                }
            } else {
                cell.removeChild(cell.childNodes[0]);
            }
        }
    }  
}