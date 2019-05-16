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
            method: 'get',
            url: "/evasys/calculate/",
            striped: true,
            cache: false,
            toolbar:"#toolbar",
            clickToSelect: true,
            showExport: true,
            exportTypes: ['excel'],
            exportDataType: 'basic',
            Icons: 'glyphicon-export',
            search: true,
            advancedSearch: true,
            idTable: 'advancedtable',
            showRefresh: true,
            showToggle: true,
            showColumns: true,
            toolbarAlign: 'right',
            buttonsAlign: 'left',
            searchOnEnterKey: true,
            singleSelect:false,
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
        $('#table1').bootstrapTable({
            method: 'get',
            url:"/evasys/calculate/",
            striped: true,
            cache: false,
            clickToSelect: true,
            showExport: true,
            exportTypes: ['excel'],
            exportDataType: 'basic',
            Icons: 'glyphicon-export',
            search: true,
            advancedSearch: true,
            idTable: 'advancedtable',
            showRefresh: true,
            showToggle: true,
            showColumns: true,
            toolbarAlign: 'right',
            buttonsAlign: 'left',
            searchOnEnterKey: true,
            singleSelect:true,
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
        var temp = {
            limit: params.limit,
            offset: params.offset,
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

