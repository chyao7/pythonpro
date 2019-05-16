$(function(){
	$('#login').dialog({
		title:'请登录',
		width:300,
		height:220,
		iconCls:'icon-login',
		modal:true,
		buttons:'#btn'
	});
	$('#username').validatebox({
		required:true,
		missingMessage:'请输入账号',
		invalidMessage:'用户账号不得为空',
	});
	$('#password').validatebox({
		required:true,
		validType:'length[6,30]',
		missingMessage:'请输入密码',
		invalidMessage:'密码为6到30位数字或字母',
	});

	if (!$('#member').validatebox('isValid')) {
		$('#member').focus();
	} else if (!$('#password').validatebox('isValid')) {
		$('#password').focus();
	}
	
});