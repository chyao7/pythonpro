$(function(){
	$('#reg').dialog({
		title:'请注册',
		width:400,
		height:400,
		iconCls:'icon-login',
		modal:true,
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
			invalidMessage:'请输入6到30位数字或字母',
	});
	//邮箱验证
	$('#email').validatebox({
		required:true,
		validType:'length[6,30]',
		missingMessage:'请输入邮箱',
		invalidMessage:'请输入规范的邮箱地址',
	});
	//信用代码验证
	$('#companyid').validatebox({
		required:true,
		validType:'length[18,18]',
		missingMessage:'请输入公司信用代码',
		invalidMessage:'18位信用代码',
	});
	//加载页面时判断
	if (!$('#username').validatebox('isValid')) {
		$('#btn').linkbutton({
			disabled:false,
		});
		$('#username').focus();
	} else if (!$('#password').validatebox('isValid')) {
		$('#password').focus();
	}
	
	
});