$(function(){
	$('#table').bootstrapTable({
		method: 'get',
		url:"/evasys/defindex/",
		striped: true,
		cache: false,
		clickToSelect:true,
		showExport: true,
		exportTypes:['excel','xlsx'],
		exportDataType:'basic',
        Icons:'glyphicon-export',
		search:true,
		advancedSearch:true,
		idTable:'advancedtable',
		showRefresh: true,
		showToggle: true,
		showColumns: true,
		toolbarAlign: 'right',
		buttonsAlign:'left',
		searchOnEnterKey: true
	});
});
