$(function () {
    var oTable = new TableInit();
    oTable.Init();
    var oButtonInit = new ButtonInit();
    oButtonInit.Init();
});
var TableInit =function(){
	var oTableInit = new Object();
	oTableInit.Init = function () {
        $('#table').bootstrapTable({
            method: 'get',                      //请求方式（*）
            url: "/evasys/resshow/",
            toolbar: '#toolbar',
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
            clickToSelect: true,
            showExport: true,                     //是否显示导出
            search: true,
            advancedSearch: true,
            idTable: 'advancedtable',
            showRefresh: true,
            showToggle: true,
            showColumns: true,
            toolbarAlign: 'right',//toolbar位置
            buttonsAlign: 'left', //刷新按钮位置
            searchOnEnterKey: true,
            singleSelect:true
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
