/**
 * Created by kw107 on 2015/12/28.
 */
$(document).ready(function()
{
    var doc=$('html').addClass('js-login'),
        container = $('#container-login'),
        formLogin = $('#form-login'),
        centered;

    /*This function will handle the login process through AJAX*/
    formLogin.submit(function(event)
    {
        var login = $.trim($('#login').val()),
            pass = $.trim($('#pass').val());
        //check inputs
        if (login.length == 0)
        {
            alert('Please fill in your login');
            return false;
        }
        else if (pass.length == 0)
        {
            alert('Please fill in your login');
            return false;
        }
        else
        {
//                  formLogin.clearMessages();
            event.preventDefault();
            //The AJAX calls
            $.ajax({url: "/interests/login/",
                type: "post",
                data: {
                    Username: login,
                    Password: pass
                },
                success: function(msg)
                {
                    var data = $.parseJSON(msg)

                    if (data.code == "0")
                    {
                        document.location.href = '/admin/'
                    }
                    else
                    {
                        alert('Invalid user/password, please try again');
                    }
                },
                error: function()
                {
                    alert('Error while contacting server, please try again');
                }
            });

            setTimeout(function()
            {
                document.location.href = './'
            }, 2000);
        }
    });
})