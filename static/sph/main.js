$(document).ready(function(){
    
myStorage = window.localStorage;
for (var i =41;i<=101;i++){
    myStorage.setItem(i,0);
}
    
    $(".slider").slider({
        stop:function(event,ui){
            myStorage.setItem(event.target.id,ui.value);
            
        }
    });



$('#save_button').on('submit', function(event){
    alert("AHAHA");
   
    console.log("form submitted!");  // sanity check
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
    education = $("input[type='radio'][name='educaiton']:checked").val();
    expenditures = $("input[type='radio'][name='money']:checked").val();
    occupation = $("input[type='radio'][name='job']:checked").val();
    
    // data sent with the post request

        // handle a successful response
   var list = []
   Object.keys(myStorage).forEach(function(key){
   list[key]=myStorage.getItem(key);
});
    var data ={ gender:gender,family:family,age:age,education:education,expenditures:expenditures,occupation:occupation,storage:list};

   
     $.ajax({
        url : "/person/new/", // the endpoint
        type : "POST", // http method
        data : JSON.stringify(data), // data sent with the post request

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