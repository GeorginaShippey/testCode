$(document).ready( function() {
    /*
    $("#id_groups option").each(function() {
        if($(this).is(':not(:selected)')) {
        $(this).remove();
        }
    });
    */
    alert("js");
    var x = $("#id_client").val();
    $("#id_client").on('change', function() {
        alert("hi");
        $('#id_groups_from').append($('<option></option>').attr({'value':'1', 'title':'Group A1'}).text("Group A1"));
        //$(".selector :input").attr('disabled', true);
        });
    /*
    $("#lookup_id_client").on('click', function() {
        alert("hi");
        $('#id_groups_from').append($('<option></option>').attr({'value':'1', 'title':'Group A1'}).text("Group A1"));
        //$(".selector :input").attr('disabled', true);
        });
    $(".related-widget-wrapper").click( function() {
        var x = $("#id_client").val();
        alert(x);
        });
        */
        /*
        $("#id_groups option").each(function() {
        if($(this).is(':not(:selected)')) {
            $(this).remove();
            }
        });//id_groups option
        var csrf = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: "/test_admin/",
            dataType: "json",
            data: { "client_id": x,'csrfmiddlewaretoken':csrf},
            success: function(data) {
                var options = [];
                for (var i = 1; i < data.length + 1; i++) {
                    $('#id_groups').append($('<option></option>').attr('value',i).text(data[i-1]['fields'].name));
                }//for
            }//data function
        });//ajax
    });//client on change
    */
    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
        
 });//end
 
 
