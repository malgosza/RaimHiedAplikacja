function wyslij(){
//    var opcja = $('input[name=Plec]:checked')[0].labels[0].innerText;
//    var opcja1=$('input[name="Jak oceniasz swój sposób odżywiania?"]:checked')[0].labels[0].innerText;

   var pytanie=$('#ankieta')[0];
   var dane={};

    for(var i=0; i<pytanie.length;i++){

        if(pytanie[i].type=="button"){
            break;
        }
        var p=pytanie[i].name;
        if(pytanie[i].type=="text"){
            dane[p]=pytanie[i].value;
        }
        else{
            var zaznaczonaOdp=$('input[name="'+p+'"]:checked')[0].labels[0].innerText;
            dane[p]=zaznaczonaOdp;
        }
    }

     console.log(dane);
//    $.ajax({
//                url: "/wyslijDane",
//                success: function (result) {
//                    console.log("sie udalo sie");
//                },
//                type        : "POST", //typ połączenia
//                contentType : 'aplication/json', //gdy wysyłamy dane czasami chcemy ustawić ich typ
//                dataType    : 'json', //typ danych jakich oczekujemy w odpowiedzi
//                data        :  JSON.stringify({'Plec':'kot'})//dane do wysyłki
//
//            });
 var xhr = new XMLHttpRequest();

    xhr.open("POST", '/wyslijDane', false);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status == 200) {
            // var json = JSON.parse(xhr.responseText);
            // console.log("zwrotka: "+json.dane);
//            callback(xhr.status);
        }
    };

    var data = JSON.stringify(dane);
    xhr.send(data);
}

