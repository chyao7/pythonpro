$(document).ready(function() {
    $('#defaultForm').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            companyname: {
                message: '公司名称不是有效输入',
                validators: {
                    notEmpty: {
                        message: '公司名称不能为空'
                    },
                    regexp: {
                        regexp: /[\u4e00-\u9fa5],{0,}$/,
                        message: '公司名称只能为汉字'
                    }
                }
            },

            liscom_code: {
                message: '上市公司代码不是有效输入',
                validators: {
                    notEmpty: {
                        message: '上市公司代码不能为空，如果公司为非上市公司默认为000000'
                    },
                    stringLength: {
                        min: 6,
                        max: 6,
                        message: '上市公司代码为六位'
                    },
                    regexp: {
                        regexp: /[0-9]+$/,
                        message: '上市公司代码只能为数字'
                    }
                }
            },

            telephone: {
                validators: {
                    notEmpty: {
                        message: '公司热线不能为空'
                    },
                    stringLength: {
                        min: 8,
                        max: 16,
                        message: '公司热线为8到11位'
                    },
                    regexp: {
                        regexp: /[0-9/()-]+$/,
                        message: '公司热线只能为数字、()、-'
                    }
                }
            },

            website: {
                message: '公司网址不是有效输入',
                validators: {
                    stringLength: {
                        min: 0,
                        max: 100,
                        message: '公司网址应在100字符以内'
                    },
                    regexp: {
                        regexp: /(http|https):\/\/www.[A-Za-z0-9.$?\/]*.(com|cn)/,
                        message: '您输入的网址不合法'
                    }
                }
            },

            introdution: {
                message: '公司简介不是有效输入',
                validators: {
                    notEmpty: {
                        message: '公司名称不能为空'
                    },
                    stringLength: {
                        min: 50,
                        max: 500,
                        message: '公司简介字数在50到500字'
                    },
                    regexp: {
                        regexp: /[\u4e00-\u9fa5],{0,}$/,
                        message: '公司简介只能为汉字'
                    }
                }
            },

             username: {
                message: '用户名不是有效输入',
                validators: {
                    notEmpty: {
                        message: '用户名不能为空'
                    },
                    stringLength: {
                        min: 2,
                        max: 10,
                        message: '用户名字数在2到10字'
                    },
                    regexp: {
                        regexp: /[\u4e00-\u9fa5],{0,}$/,
                        message: '用户名只能为汉字'
                    }
                }
            },

            email: {
                validators: {
                    notEmpty: {
                        message: 'The email address is required and can\'t be empty'
                    },
                    emailAddress: {
                        message: 'The input is not a valid email address'
                    }
                }
            },

            emailcode: {
                validators: {
                    notEmpty: {
                        message: '验证码不能为空'
                    }
                }
            },

            password: {
                validators: {
                    notEmpty: {
                        message: '密码不能为空'
                    },
                    stringLength: {
                        min: 6,
                        max: 17,
                        message: '密码必须大于6位小于17位'
                    },
                    regexp: {
                        regexp: /[A-Za-z].*[0-9]|[0-9].*[A-Za-z]/,
                        message: '密码必须同时包含数字和字母'
                    },
                    identical: {
                        field: 'confirmPassword',
                        message: '两次密码输入不一致'
                    }
                }
            },

            repassword: {
                validators: {
                    notEmpty: {
                        message: '确认密码不能为空'
                    },
                    identical: {
                        field: 'password',
                        message: '两次密码输入不一致'
                    }
                }
            }
        }
    });
});
