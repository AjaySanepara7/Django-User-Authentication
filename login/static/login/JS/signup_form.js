$(document).ready(function(){
    $("#submit").click(function(e){
        validation()
    })

    $("#change_password").click(function(e){
        change_password_validation()
    })
    
    function validation(){
        $("#signupForm").validate({
            rules: {
                username: {
                    required: true,
                    minlength: 2
                },
                firstname: "required",
                lastname: "required",
                password: {
                    required: true,
                    minlength: 5
                },
                confirm_password: {
                    required: true,
                    minlength: 5,
                    equalTo: "#password"
                },
                email: {
                    required: true,
                    email: true
                },
                date_of_birth: {
                    required: true,
                    date: true,
                    dateFormat: true
                },
                gender: "required",
                hobby: "required"
            },
            messages: {
                username: {
                    required: "Please enter a username",
                    minlength: "Your username must consist of at least 2 characters"
                },
                firstname: {
                    required: "Please enter a firstname",
                },
                lastname: {
                    required: "Please enter a lastname",
                },
                password: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long"
                },
                confirm_password: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long",
                    equalTo: "Please enter the same password as above"
                },
                date_of_birth: {
                    required: "Please enter Date of Birth",
                },
                gender: "Please select your gender",
                hobby: "Please select atleast one hobby"
            }
        })
    }

    function change_password_validation(){
        $("#change_password").validate({
            rules: {
                username: {
                    required: true,
                    minlength: 2
                },
                current_password: {
                    required: true,
                },
                password: {
                    required: true,
                    minlength: 5
                },
                confirm_password: {
                    required: true,
                    minlength: 5,
                    equalTo: "#password"
                },
            },
            messages: {
                username: {
                    required: "Please enter a username",
                    minlength: "Your username must consist of at least 2 characters"
                },
                current_password: {
                    required: "Please provide a password",
                },
                password: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long"
                },
                confirm_password: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long",
                    equalTo: "Please enter the same password as above"
                },
            }
        })
    }
    
})