$(function(){
	// nav active
	var pgurl = window.location.href.split('/')
    var pageContent = ''
	if(pgurl.length > 4) {
		pageContent = pgurl[pgurl.length - 2]
	}

	var active = '/' + pageContent
	$("nav a").each(function(){
		if($(this).attr("href") == active)
			$(this).addClass("active");
	})

    $(".get").click(function(event){
        event.preventDefault();
        var data_id = $(this).attr('data-id')
        console.log(data_id)
        url = '/' + pageContent + 'GetContent'
        console.log(url)
        $.get(url, {'data_id': data_id}, function(ret){
            $("#content").html(ret)
        })
    })

	// $("#login_form").validate({  
 //        rules: {  
 //            username: "required",  
 //            password: {  
 //                required: true,  
 //                minlength: 5  
 //            },  
 //        },  
 //        messages: {  
 //            username: "请输入姓名",  
 //            password: {  
 //                required: "请输入密码",  
 //                minlength: jQuery.format("密码不能小于{0}个字 符")  
 //            },  
 //        }  
 //    });  
 //    $("#register_form").validate({  
 //        rules: {  
 //            username: "required",  
 //            password: {  
 //                required: true,  
 //                minlength: 5  
 //            },  
 //            rpassword: {  
 //                equalTo: "#register_password"  
 //            },  
 //            email: {  
 //                required: true,  
 //                email: true  
 //            }  
 //        },  
 //        messages: {  
 //            username: "请输入姓名",  
 //            password: {  
 //                required: "请输入密码",  
 //                minlength: jQuery.format("密码不能小于{0}个字 符")  
 //            },  
 //            rpassword: {  
 //                equalTo: "两次密码不一样"  
 //            },  
 //            email: {  
 //                required: "请输入邮箱",  
 //                email: "请输入有效邮箱"  
 //            }  
 //        }  
 //    }); 

    
})