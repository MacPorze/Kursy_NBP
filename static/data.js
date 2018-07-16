$(function(){
    draw_table();
});

function draw_table(){
    $.ajax({
        type: 'GET',
        url: 'http://localhost:8000/data'
    })
        .done(function(response){
            removeChilds("tableA");
            removeChilds("tableB");
            respA = response.A
            for (i = 0; i<respA.length; i++){
                draw_raw(respA[i],'A')
            }
            respB = response.B
            for (i = 0; i<respB.length; i++){
                draw_raw(respB[i],'B')
            }
        })
        .fail(function () {
            alert("fail")
        })
}

function draw_raw(data, id){
    var para = document.createElement("tr")

    var para2 = document.createElement("td")
    var textnode = document.createTextNode(data.name)
    para2.appendChild(textnode)
    para.appendChild(para2)

    var para2 = document.createElement("td")
    var textnode = document.createTextNode(data.code)
    para2.appendChild(textnode)
    para.appendChild(para2)

    var para2 = document.createElement("td")
    var textnode = document.createTextNode(data.rate)
    para2.appendChild(textnode)
    para.appendChild(para2)

    var para2 = document.createElement("td")
    var textnode = document.createTextNode(data.date)
    para2.appendChild(textnode)
    para.appendChild(para2)

    var parent = document.getElementById("table" + id)
    parent.appendChild(para)
}

function removeChilds(id){
    var list = document.getElementById(id);
    while(list.firstChild){
        list.removeChild(list.firstChild);
    }
}

function update(){
    $.ajax({
        url:"http://localhost:8000/update"
    })
        .done(function(){
            alert("Pobrano nowe kursy")
            draw_table()
        })
        .fail(function () {
            alert("Pobieranie nowych kursów nie powiodło się")
        })


}