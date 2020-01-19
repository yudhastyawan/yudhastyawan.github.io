//const content = {
//    "1" : "content.html",
//    "2" : "content2.html"
//};
//

const change = 
    function (des) {
        $.get('ajax/'+des, function(data){
                $('#changeMain').html(data);
        });
    };
//$(document).ready(
//            
////    function(){
////    //event ketika keyword ditulis
////    });
//        change('#categorya','content.html'),
//    change('#categoryb','contentb.html')
//);

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const product = urlParams.get('p');
if(product!==null){
    change(content[product])
};