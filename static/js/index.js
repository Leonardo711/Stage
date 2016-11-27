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

    var progressDataId = ''

    $(".get").click(function(event){
        event.preventDefault();
        var data_id = $(this).attr('data-id')
        // console.log(data_id)
        var url = '/' + 'getContent'
        // console.log(url)
        $.get(url, {'data_id': data_id, 'page': pageContent}, function(ret){
            console.log(ret)
            if(pageContent == 'project'){
                ret = JSON.parse(ret)
                // console.log(ret.basicInformation)
                progressDataId = ret.data_id
                $("#content").html(ret.basicInformation)
            } else {
                $("#content").html(ret)
            }
        })
    })

    $("#to-progress").click(function(){
        sessionStorage.setItem('data_id', progressDataId)
    })

    $(".language").click(function(event){
        event.preventDefault();
        var language = this.id
        var url = '/' + 'language'
        console.log(language)
        console.log(url)
        $.get(url, {'language': language, 'page': pageContent}, function(ret){
            console.log(ret)
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