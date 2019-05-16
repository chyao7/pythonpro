$(function () {

    //1.初始化Table
    var oTable = new TableInit();
    oTable.Init();
    //2.初始化Button的点击事件
    var oButtonInit = new ButtonInit();
    oButtonInit.Init();

});
var TableInit =function(){
	var oTableInit = new Object();
	oTableInit.Init = function () {
        $('#table').bootstrapTable({
            method: 'get',                      //请求方式（*）
            url: "/evasys/chanindex/",
            toolbar: '#toolbar',
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
            clickToSelect: true,
            showExport: true,                     //是否显示导出
            exportTypes: ['excel','xlsx'],  //导出文件类型
            exportDataType: 'basic',
            Icons: 'glyphicon-export',
            search: true,
            advancedSearch: true,
            idTable: 'advancedtable',
            showRefresh: true,
            showToggle: true,
            showColumns: true,
            toolbarAlign: 'right',//toolbar位置
            buttonsAlign: 'left', //刷新按钮位置
            searchOnEnterKey: true,
            onEditableSave: function (field, row, oldValue, $el) {
                $.ajax({
                    type: "post",
                    url: "/Editable/chanindex/",
                    data: {strJson: JSON.stringify(row)},
                    success: function (data, status) {
                        if (status == "success") {
                            alert("编辑成功");
                        }
                    },
                    error: function () {
                        alert("Error");
                    },
                    complete: function () {

                    }

                });
            }

        });
    };
	oTableInit.queryParams = function (params) {
        var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
            limit: params.limit,   //页面大小
            offset: params.offset,  //页码
            departmentname: $("#txt_search_departmentname").val(),
            statu: $("#txt_search_statu").val()
        };
        return temp;
    };
    return oTableInit;


};
var ButtonInit = function () {
    var oInit = new Object();
    var postdata = {};

    oInit.Init = function () {

    };

    return oInit;
};
