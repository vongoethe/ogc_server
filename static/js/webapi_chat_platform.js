$.chat_platform = {};
$.chat_platform.HOST = 'yncaiyun1.com';
$.chat_platform.PROTOCOL = 'http';
$.chat_platform.WS_PROTOCOL = 'ws';
$.chat_platform.PORT = '8091';
$.chat_platform.DEBUG = true;
$.chat_platform.ME_PREFIX = '我';
$.chat_platform.SYSTEM_PREFIX = '[系统]';
$.chat_platform.chat_options = {};


$.chat_platform.post_cors = function(action, data, callback)
{
    var url = $.chat_platform.PROTOCOL + '://' + $.chat_platform.HOST + ':' + $.chat_platform.PORT + '/' + action;
    $.ajax({
        url: url,
        type: "post",
        data: encodeURIComponent(JSON.stringify(data)),
        crossDomain: true,
        xhrFields: {
            withCredentials: true
        },        
        dataType: "text",
        success: function(data1){
            if(callback)
            {
                var ret = JSON.parse(decodeURIComponent(data1));
                callback(ret);
            }
        }
    });
};

$.chat_platform.user_get = function(data, callback)
{
	$.chat_platform.post_cors('user_get', data, callback);
};

$.chat_platform.group_get = function(data, callback)
{
	$.chat_platform.post_cors('group_get', data, callback);
};


$.chat_platform.user_add = function(data, callback)
{
    if(data['username'] === undefined)
    {
        throw "username_required";
    }
    if(data['password'] === undefined)
    {
        throw "password_required";
    }
	$.chat_platform.post_cors('user_add', data, callback);
};

$.chat_platform.user_update = function(data, callback)
{
    if(data['_id'] === undefined)
    {
        throw "user_id_required";
    }
	$.chat_platform.post_cors('user_update', data, callback);
};
$.chat_platform.user_remove = function(data, callback)
{
    if(data['_id'] === undefined)
    {
        throw "user_id_required";
    }
    if(data['password'] === undefined)
	$.chat_platform.post_cors('user_remove', data, callback);
};

//$.chat_platform.offline = function(data, callback)
//{
    //if(data['_id'] === undefined)
    //{
        //throw "user_id_required";
    //}
    //$.chat_platform.post_cors('offline', data, callback)
//};

$.chat_platform.user_contact_get = function(data, callback)
{
    if(data['_id'] === undefined)
    {
        throw "user_id_required";
    }
	//data['user_detail'] = true;
    $.chat_platform.post_cors('user_contact_get', data, callback)
};

$.chat_platform.user_group_get = function(data, callback)
{
    if(data['_id'] === undefined)
    {
        throw "user_id_required";
    }
	data['user_detail'] = true;
    $.chat_platform.post_cors('user_group_get', data, callback)
};
$.chat_platform.group_get = function(data, callback)
{
    //if(data['_id'] === undefined)
    //{
        //throw "user_id_required";
    //}
    $.chat_platform.post_cors('group_get', data, callback)
};
$.chat_platform.group_add = function(data, callback)
{
    if(data['owner_id'] === undefined)
    {
        throw "owner_id_required";
    }
    if(data['group_name'] === undefined)
    {
        throw "group_name_required";
    }
    $.chat_platform.post_cors('group_add', data, callback)
};

$.chat_platform.group_remove = function(data, callback)
{
    if(data['_id'] === undefined)
    {
        throw "group_id_required";
    }
    $.chat_platform.post_cors('group_remove', data, callback)
};

$.chat_platform.group_update = function(data, callback)
{
    if(data['_id'] === undefined)
    {
        throw "group_id_required";
    }
	$.chat_platform.post_cors('group_update', data, callback);
};


$.chat_platform.offline = function(data,  offline_callback)
{
	if($.chat_platform.websocket)
	{
		if(data.username)
		{
			$.chat_platform.websocket.send(JSON.stringify({op:'chat/offline',username:data.username}));
		}
		else if(data._id)
		{
			$.chat_platform.websocket.send(JSON.stringify({op:'chat/offline',_id:data._id}));
		}
		if(data.username || data._id)
		{
			$.chat_platform.websocket.close();
			$.chat_platform.websocket = undefined;
			offline_callback();
		}
	}
};


$.chat_platform.chat = function(options){
	if($.chat_platform.current_user === undefined)
	{
		var s =  "$.chat_platform.current_user must be set.\n";
		s += "For example:\n";
		s += "$.chat_platform.current_user = 'user1';";
		throw s;
	}
	if(! options.on_online instanceof Function)
	{
		var s = "options.on_online must be defined.\n ";
		s += "options.on_online = function(data){\n";
		s += "	data._id //current user's id(string)\n";
		s += "	data.username //current user's unique username(string)\n";
		s += "	data.display_name //current user's display name(string)\n";
		s += "	data.person_info //current user's personal info(object)\n";
		s += "	data.avatar //current user's head icon(string)\n";
		s += "	data.contacts //current user's contacts list(list)\n";
		s += "	data.groups //current user's groups list(list) if it has\n";
		s += "	data.op //it is 'chat/online' in this case\n";
		s += "};\n";
		throw s;
	}
	//if(! options.on_offline instanceof Function)
	//{
		//var s = "options.on_online must be defined.\n ";
		//s += "options.on_online = function(data){\n";
		//s += "	data._id //current user's id(string)\n";
		//s += "	data.op //it is 'chat/online' in this case\n";
		//s += "};\n";
		//throw s;
	//}
	if(! options.on_info_online instanceof Function)
	{
		var s = "options.on_info_online must be defined.\n ";
		s += "options.on_info_online = function(data){\n";
		s += "	data.from //user's id who inform this online event(string)\n";
		s += "	data.op //it is 'chat/info/online' in this case\n";
		s += "};\n";
		throw s;
	}
	if(! options.on_info_offline instanceof Function)
	{
		var s = "options.on_info_offline must be defined.\n ";
		s += "options.on_info_offline = function(data){\n";
		s += "	data.from //user's id who inform this offline event(string)\n";
		s += "	data.op //it is 'chat/info/offline' in this case\n";
		s += "};\n";
		throw s;
	}
};


$.chat_platform.init_websocket = function(data, message_callback, error_callback)
{
	if(data.username === undefined && data._id === undefined)
	{
		console.log('username or id required');
		return;
	}
	data['op'] = 'chat/online';
	data['inform_contact'] = true;
	var wsurl =  $.chat_platform.WS_PROTOCOL + "://" + $.chat_platform.HOST + ":" + $.chat_platform.PORT + "/websocket";
	if($.chat_platform.websocket === undefined)
	{
		$.chat_platform.websocket = new WebSocket(wsurl);
	}
	if($.chat_platform.websocket)
	{
		$.chat_platform.websocket.onopen = function() 
		{
			$.chat_platform.websocket.send(JSON.stringify(data));
		};
		$.chat_platform.websocket.onclose = function(e) 
		{
			console.log("websocket close");
		};
		$.chat_platform.websocket.onerror = function(e) 
		{
			console.log("websocket error:" + e);
			$.chat_platform.websocket.close();
			error_callback(e);
		};
		$.chat_platform.websocket.onmessage = function(e) 
		{
			if(e.data.length>0)
			{
				var obj = JSON.parse(e.data);
				if(obj instanceof Array)
				{
				}
				if(obj instanceof Object)
				{
					if(obj.result)
					{
						error_callback(obj.result);
					}
					else
					{
						message_callback(obj);
					}
				}
				
			}else
			{
			//$.chat_platform.websocket.send(JSON.stringify({}));
				$.chat_platform.websocket.send('');
			}
		};
	}		
};



if($.chat_platform.DEBUG)
{

	function update_user_list(data)
	{
		$('select[id^=current_user_]').empty();
		$('select[id^=user_list_]').empty();
		var s = '';
		for(var i in data)
		{
			s += '<option value="' + data[i]['_id'] + '">' + data[i]['display_name'] + '</option>';
		}
		$('select[id^=current_user_]').append(s);
		$('select[id^=user_list_]').append(s);
		
        $('#current_user_2').off();
        $('#current_user_2').on('change', function(){
			$.chat_platform.user_contact_get({_id:$(this).val(), user_detail:true}, function(data1){
				//console.log(data1);
				$('#current_contact_2').empty();
				var s = '';
				for(var i in data1)
				{
					s += '<option value="' + data1[i]['_id'] + '">' + data1[i]['display_name'] + '</option>';
				}
				$('#current_contact_2').append(s);
			});
        });
		$('#current_user_2').trigger('change');
	}
	
	function update_group_list(data)
	{
		$('select[id^=current_group_]').empty();
		$('select[id^=group_list_]').empty();
		var s = '';
		for(var i in data)
		{
			s += '<option value="' + data[i]['_id'] + '">' + data[i]['group_name'] + '</option>';
		}
		$('select[id^=current_group_]').append(s);
		$('select[id^=group_list_]').append(s);
		
        $('#current_group_4').off();
        $('#current_group_4').on('change', function(){
			$.chat_platform.group_get({_id:$(this).val(),user_detail:true}, function(data1){
				//console.log(data1);
				if(data1.result)
				{
					alert(data1.result);
				}
				else if(data1.length>0)
				{
					members = data1[0]['members'];
					$('#user_group_4').empty();
					var s = '';
					for(var i in members)
					{
						s += '<option value="' + members[i]['_id'] + '">' + members[i]['display_name'] + '</option>';
					}
					$('#user_group_4').append(s);
				}
			});
        });
		$('#current_group_4').trigger('change');
		$('#group_list_7').off();
        $('#group_list_7').on('change', function(){
			$.chat_platform.group_get({_id:$(this).val(),user_detail:true}, function(data1){
				if(data1.result)
				{
					alert(data1.result);
				}
				else if(data1.length>0)
				{
					members = data1[0]['members'];
					$('#user_group_7').empty();
					var s = '';
					for(var i in members)
					{
						s += '<option value="' + members[i]['_id'] + '">' + members[i]['display_name'] + '</option>';
					}
					$('#user_group_7').append(s);
				}
			});
		});
	}
	
	function update_online_list()
	{
		$.chat_platform.post_cors('user_get', {user_detail:true}, function(data1){
			if(data1.result)
			{
				alert(data1.result);
			}else
			{
				$('#online_list_5').empty();
				var s = '';
				for(var i in data1)
				{
					if(data1[i].online_status === 'online')
					{
						s += '<option value="' + data1[i]._id + '">' + data1[i].display_name + '</option>';
					}
				}
				$('#online_list_5').append(s);
			}
		});
	}
	
	function update_contact_list(data)
	{
		
		if(data.result)
		{
			alert(data.result);
			return;
		}
		if((data.op === 'chat/online' || data.op === 'chat/response/contact/add/accept' || data.op === 'chat/request/contact/remove') && data.contacts)
		{
			$('#current_contact_6').empty();
			var s = '';
			for(var i in data.contacts)
			{
				var status = '';
				if(data['contacts'][i]['online_status'] === 'online')
				{
					status = '(在线)';
				}
				s += '<option value="' + data['contacts'][i]['_id'] + '">' + data['contacts'][i]['display_name'] + status + '</option>';
			}
			$('#current_contact_6').append(s);
		}
		if(data.op === 'chat/info/online' && data['from'])
		{
			var id = data['from'];
			var text = $('#current_contact_6 option[value="' + id + '"]').text();
			if(text && text.indexOf('(在线)') < 0)
			{
				$('#current_contact_6 option[value="' + id + '"]').text(text + '(在线)');
			}
		}
		if(data.op === 'chat/info/offline' && data['from'])
		{
			var id = data['from'];
			var text = $('#current_contact_6 option[value="' + id + '"]').text();
			if(text && text.indexOf('(在线)') > -1)
			{
				text = text.replace('(在线)', '');
				$('#current_contact_6 option[value="' + id + '"]').text(text);
			}
		}
	}
	
	function get_select_text(sel_id, value)
	{
		var ret = value;
		var text = $('#' + sel_id + ' option[value="' + value + '"]').text();
		if(text)
		{
			if(text.indexOf('(在线)') > -1)
			{
				text = text.replace('(在线)', '');
			}
			ret = text;
		}
		return ret;
	}
	
    $(function() {
	
	
		
	
	
	
	
	
	
	
	
	
	
		$.chat_platform.post_cors('user_get', {}, function(data1){
			if(data1.result)
			{
				alert(data1.result);
			}else
			{
				update_user_list(data1);
			}
		});
		$.chat_platform.post_cors('group_get', {}, function(data1){
			if(data1.result)
			{
				alert(data1.result);
			}else
			{
				update_group_list(data1);
			}
		});
		
		
    
        $('#btn_user_add').on('click', function(){
			var username = $('#username').val();
			var password = $('#password').val();
			if(username.length>0 && password.length>0 )
			{
				$.chat_platform.user_add({username:username, password:password}, function(data1){
					console.log(data1);
				});
			}
        });
        $('#btn_user_remove').on('click', function(){
			if(confirm("确定删除用户[" + $('#user_list_1').val() + "]吗?"))
			{
				$.chat_platform.user_remove({_id:$('#user_list_1').val()}, function(data1){
					console.log(data1);
				});
			}
        });
		
        $('#btn_contact_add').on('click', function(){
			var v = $('#user_list_2').val();
			var s = $('#user_list_2 option:selected').text();
			if(v)
			{
				//console.log(s);
				//console.log(v);
				var s = '<option value="' + v + '">' + s + '</option>';
				$('#current_contact_2').append(s);
			}
        });
        $('#btn_contact_remove').on('click', function(){
			//var sel = $('#current_contact_2').val();
			$('#current_contact_2 option:selected').remove();
        });
        $('#btn_contact_save').on('click', function(){
			var sel = $('#current_user_2').val();
			if(sel)
			{
				if(confirm("确定保存好友列表吗?"))
				{
					var contacts = [];
					$('#current_contact_2 option').each(function(){
						contacts.push($(this).val());
					});
					$.chat_platform.user_update({_id:sel,contacts:contacts}, function(data1){
						console.log(data1);
					});
				}
			}
        });
        $('#btn_group_add').on('click', function(){
			if($('#group_name').val().length>0 && $('#current_user_3').val() && $('#current_user_3').val().length>0)
			{
				$.chat_platform.group_add({group_name:$('#group_name').val(), owner_id:$('#current_user_3').val(),description:$('#group_description').val()}, function(data1){
					console.log(data1);
				});
			}
        });
        $('#btn_group_remove').on('click', function(){
			var sel = $('#group_list_3').val();
			if(sel)
			{
				$.chat_platform.group_remove({_id:sel}, function(data1){
					console.log(data1);
				});
			}
        });
        $('#btn_user_group_add').on('click', function(){
			var v = $('#user_list_4').val();
			var s = $('#user_list_4 option:selected').text();
			if(v)
			{
				var s = '<option value="' + v + '">' + s + '</option>';
				$('#user_group_4').append(s);
			}
        });
        $('#btn_user_group_remove').on('click', function(){
			$('#user_group_4 option:selected').remove();
        });
        $('#btn_user_group_save').on('click', function(){
			var sel = $('#current_group_4').val();
			if(sel)
			{
				if(confirm("确定保存该用户组用户列表吗?"))
				{
					var members = [];
					$('#user_group_4 option').each(function(){
						members.push($(this).val());
					});
					$.chat_platform.group_update({_id:sel,members:members}, function(data1){
						console.log(data1);
					});
				}
			}
        });
        $('#btn_user_online').on('click', function(){
			$(this).attr('disabled', 'disabled');
			$('#btn_user_offline').removeAttr('disabled');
			$('#btn_send').removeAttr('disabled');
			var sel = $('#user_list_5').val();
			$('#user_list_5').attr('disabled', 'disabled');
			if(sel)
			{
				$.chat_platform.init_websocket({_id:sel}, 
					function(data1){
						console.log(data1);
						if(data1.op === 'chat/online' || data1.op === 'chat/info/online' || data1.op === 'chat/info/offline')
						{
							update_online_list();
							update_contact_list(data1);
						}
						if(data1.op === 'chat/chat')
						{
							var from_user = get_select_text('current_contact_6', data1.from);
							$('#recv_msg').text(  $('#recv_msg').text() + '\n' + from_user + ':' + data1.msg);
						}
						if(data1.op === 'chat/request/contact/add')
						{
							if(confirm('[' + data1.display_name + ']请求你加他(她)为好友,是否同意?'))
							{
								if($.chat_platform.websocket)
								{
									$.chat_platform.websocket.send(JSON.stringify({op:'chat/response/contact/add/accept',from:data1.to, to:data1.from}));
								}
							}else
							{
								if($.chat_platform.websocket)
								{
									$.chat_platform.websocket.send(JSON.stringify({op:'chat/response/contact/add/reject',from:data1.to, to:data1.from}));
								}
							}
						}
						if(data1.op === 'chat/response/contact/add/reject')
						{
							var reason = '';
							if(data1.reject_reason)
							{
								reason = ',原因是:[' + data1.reject_reason + ']';
							}
							$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.SYSTEM_PREFIX + ':' + '[' + data1.display_name + ']已将你拒绝' + reason);
						}
						if(data1.op === 'chat/response/contact/add/accept')
						{
							//console.log(data1);
							update_contact_list(data1);
							var id = data1.from;
							var text = get_select_text('current_contact_6', id);
							$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.SYSTEM_PREFIX + ':' + '[' + text + ']已将你添加为好友');
						}
						if(data1.op === 'chat/request/contact/remove')
						{
							var id = data1.from;
							var text = get_select_text('current_contact_6', id);
							$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.SYSTEM_PREFIX + ':' + '[' + text + ']已将你从好友列表中移除');
							update_contact_list(data1);
						}
						if(data1.op === 'chat/request/group/join')
						{
							var group_name = get_select_text('group_list_7', data1.to_group);
							if(confirm('[' + data1.display_name + ']请求你加他(她)进组[' + group_name + '],是否同意?'))
							{
								if($.chat_platform.websocket)
								{
									$.chat_platform.websocket.send(JSON.stringify({op:'chat/response/group/join/accept',from:data1.to, to:data1.from, to_group:data1.to_group, request_src:data1.request_src}));
								}
							}else
							{
								if($.chat_platform.websocket)
								{
									$.chat_platform.websocket.send(JSON.stringify({op:'chat/response/group/join/reject',from:data1.to, to:data1.from, to_group:data1.to_group, request_src:data1.request_src}));
								}
							}
						}
						if(data1.op === 'chat/response/group/join/accept')
						{
							var group_name = get_select_text('group_list_7', data1.to_group);
							var new_name = get_select_text('user_list_5', data1.request_src);
							$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.SYSTEM_PREFIX + ':' + '[' + new_name + ']已成功加入组[' + group_name + ']' );
						
						}
						if(data1.op === 'chat/response/group/join/reject')
						{
							var reason = '';
							if(data1.reject_reason)
							{
								reason = ',原因是:[' + data1.reject_reason + ']';
							}
							var group_name = get_select_text('group_list_7', data1.to_group);
							$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.SYSTEM_PREFIX + ':' + '[' + data1.display_name + ']已将你拒绝加入组[' + group_name + ']' + reason);
						}
						
					},
					function(data1){
						//console.log('error_callback');
						console.log(data1);
				});
			
			}
			
        });
		$('#btn_user_offline').attr('disabled', 'disabled');
		$('#btn_send').attr('disabled', 'disabled');
		
        $('#btn_user_offline').on('click', function(){
			$('#btn_user_online').removeAttr('disabled');
			$(this).attr('disabled', 'disabled');
			$('#btn_send').attr('disabled', 'disabled');
			$('#user_list_5').removeAttr('disabled');
			if($.chat_platform.websocket)
			{
				$.chat_platform.websocket.send(JSON.stringify({op:'chat/offline',_id:$('#user_list_5').val(), inform_contact:true}));
			}
        });
        $('#btn_clear_recv').on('click', function(){
			$('#recv_msg').text('');
        });
        $('#btn_send').on('click', function(){
			var sel = $('#current_contact_6').val();
			var v = $('#send_msg').val();
			if(sel && v && v.length>0 && $.chat_platform.websocket)
			{
				$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.ME_PREFIX + ':' + v);
				$.chat_platform.websocket.send(JSON.stringify({op:'chat/chat',from:$('#user_list_5').val(),to:sel, msg:v}));
			}
			$('#send_msg').val('');
        });
        $('#btn_request_contact_add').on('click', function(){
			var to = $('#online_list_5').val();
			var from = $('#user_list_5').val();
			var text = $('#online_list_5 option:selected').text();
			if(from && to && from.length>0 && to.length>0 && $.chat_platform.websocket)
			{
				$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.ME_PREFIX + ':' + '请求添加[' + text + ']为好友,等待对方回复...');
				$.chat_platform.websocket.send(JSON.stringify({op:'chat/request/contact/add',from:from,to:to}));
			}
        });
        $('#btn_request_contact_remove').on('click', function(){
			var from = $('#user_list_5').val();
			var to = $('#current_contact_6').val();
			var text = $('#current_contact_6 option:selected').text();
			if(from && to && from.length>0 && to.length>0 && $.chat_platform.websocket)
			{
				if(confirm('你确定要从好友列表移除[' + text + ']吗?'))
				{
					$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.ME_PREFIX + ':' + '从好友列表移除[' + text + ']');
					$.chat_platform.websocket.send(JSON.stringify({op:'chat/request/contact/remove',from:from,to:to}));
				}
			}
        });
        $('#btn_group_add_request').on('click', function(){
			var from = $('#user_list_5').val();
			var to_group = $('#group_list_7').val();
			var text = $('#group_list_7 option:selected').text();
			if(from && to_group && from.length>0 && to_group.length>0 && $.chat_platform.websocket)
			{
				if(confirm('你确定要加入组[' + text + ']吗?'))
				{
					$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.ME_PREFIX + ':' + '请求加入组[' + text + '],等待确认中...');
					$.chat_platform.websocket.send(JSON.stringify({op:'chat/request/group/join',from:from,to_group:to_group}));
				}
			}
        });
        $('#btn_group_quit').on('click', function(){
			var from = $('#user_list_5').val();
			var to_group = $('#group_list_7').val();
			var text = $('#group_list_7 option:selected').text();
			if(from && to_group && from.length>0 && to_group.length>0 && $.chat_platform.websocket)
			{
				if(confirm('你确定要退出组[' + text + ']吗?'))
				{
					$('#recv_msg').text(  $('#recv_msg').text() + '\n' + $.chat_platform.ME_PREFIX + ':' + '退出组[' + text + ']');
					$.chat_platform.websocket.send(JSON.stringify({op:'chat/request/group/quit',from:from, to_group:to_group}));
				}
			}
        });
		
		
		
	});
}

