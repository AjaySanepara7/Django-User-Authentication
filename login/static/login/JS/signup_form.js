$(document).ready(function(){

    $.validator.addMethod("password_validation", function(value, element){
        const password_regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/
        return this.optional(element) || password_regex.test(value);
    }, "The password must be 8 characters long, contain one uppercase letter, one lowercase letter, one number and one special character.")


    $("#submit").click(function(e){
        debugger;
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
                    password_validation: true
                },
                confirm_password: {
                    required: true,
                    password_validation: true,
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
                    password_validation: "The password must be 8 characters long, contain one uppercase letter, one lowercase letter, one number and one special character.",
                },
                confirm_password: {
                    required: "Please provide a password",
                    password_validation: "The password must be 8 characters long, contain one uppercase letter, one lowercase letter, one number and one special character.",
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
                    password_validation: true
                },
                confirm_password: {
                    required: true,
                    password_validation: true,
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
                    password_validation: "The password must be 8 characters long, contain one uppercase letter, one lowercase letter, one number and one special character."
                },
                confirm_password: {
                    required: "Please provide a password",
                    password_validation: "The password must be 8 characters long, contain one uppercase letter, one lowercase letter, one number and one special character.",
                    equalTo: "Please enter the same password as above"
                },
            }
        })
    }
    
})