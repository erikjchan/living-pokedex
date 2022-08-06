function reset() { 
    if (typeof boxNumber === 'undefined') {
            boxNumber = "1"
        }
        box = document.getElementById("box");
        document.getElementById("boxTitle").innerHTML = "Box " + boxNumber;
        boxList = pokemonList[boxNumber];
        for(var i = 0; i < box.rows.length; i++) {
          for(var j = 0; j < box.rows[i].cells.length; j++) {
            let cell = box.rows[i].cells[j];
            boxIndex = (i*6) + j;
            if (boxIndex < boxList.length) {
                pokemon = boxList[boxIndex];
                let img = document.createElement("img");
                img.src = pokemon['image'];
                // img.alt = item['number'] + '. ' + item['name'];
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