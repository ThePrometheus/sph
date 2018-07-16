myStorage = window.localStorage;
for (var i =41;i<=101;i++){
    myStorage.setItem(i,0);
}
$(document).ready(function(){
    

    
    $(".slider").slider({
        stop:function(event,ui){
            var pos=0;
            if (ui.value>50){
                pos=(ui.value-50)+((ui.value-50)*2);
            }if(ui.value<=50){
                pos=(ui.value-50)-((50-ui.value)*2);
            }
            myStorage.setItem(event.target.id,ui.value);
            
        }
    });



$('#save_button').click(function(event){
    
    create_person();
});

var gender;
var family;
var education;
var age;
var expenditures;
var occupation;
function create_person(){
gender=$("input:radio[name='gender']:checked").val();
    family = $("input[type='radio'][name='family']:checked").val();
    age = $("input[type='radio'][name='age']:checked").val();
    
    education = $("input[type='radio'][name='education']:checked").val();
    expenditures = $("input[type='radio'][name='money']:checked").val();
    occupation = $("input[type='radio'][name='occupation']:checked").val();
    alert(occupation);
    
    // data sent with the post request

        // handle a successful response
   var list = [];
   Object.keys(myStorage).sort().forEach(function(key){
   list.push(key,myStorage.getItem(key));
   
    console.log(list);
    
    
});
    var temp ={ gender:gender,family:family,age:age,education:education,expenditures:expenditures,occupation:occupation,questions:list};
    var data = temp;
    console.log(data);
   
     $.ajax({
        url : "/sph/person/new/", // the endpoint
        type : "POST",// http method
        data: data, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
    
};
    
    
    
    
    });