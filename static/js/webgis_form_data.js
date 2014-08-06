var g_zaware = false;

//绝缘子串
var g_insulator_type_list = [
	{'value':'导线绝缘子','label':'导线绝缘子', 'py':'dxjyzc'},
	{'value':'跳线绝缘子','label':'跳线绝缘子', 'py':'txjyzc'},
	{'value':'地线绝缘子','label':'地线绝缘子', 'py':'dxjyzc'},
	{'value':'OPGW绝缘子','label':'OPGW绝缘子', 'py':'opgwjyzc'}
];
var g_mat_type_list = [
	{'value':'陶瓷','label':'陶瓷', 'py':'tc'},
	{'value':'玻璃','label':'玻璃', 'py':'bl'},
	{'value':'合成','label':'合成', 'py':'hc'},
	{'value':'未知','label':'未知', 'py':'wz'}
];
var g_insulator_flds = [
	{display: "类型", id: "type", newline: true,  type: "text", editor:{readonly:true}, group:'绝缘子', width:350, labelwidth:105},
	{display: "绝缘子类型", id: "insulator_type", newline: true,  type: "select", editor: {data:g_insulator_type_list}, group:'绝缘子',  width:350, labelwidth:105},
	{display: "绝缘子材料", id: "material", newline: true,  type: "select", editor: {data:g_mat_type_list}, group:'绝缘子',  width:350, labelwidth:105},
	{display: "绝缘子型号", id: "model", newline: true,  type: "text", group:'绝缘子', width:350, labelwidth:105},
	{display: "串数", id: "strand", newline: true,  type: "spinner", step:1, min:0,max:100, group:'绝缘子', width:90, validate:{number: true}, labelwidth:105},
	{display: "片数", id: "slice", newline: false,  type: "spinner", step:1, min:0,max:500, group:'绝缘子', width:90, validate:{number: true}, labelwidth:105},
	{display: "生产厂家", id: "manufacturer", newline: true,  type: "text", group:'绝缘子', width:350, labelwidth:105},
	{display: "组装图号", id: "assembly_graph", newline: true,  type: "text", group:'绝缘子', width:350, labelwidth:105}
];
//防振锤
var g_damper_list = [
	{'value':'导线大号侧','label':'导线大号侧'},
	{'value':'导线小号侧','label':'导线小号侧'},
	{'value':'地线大号侧','label':'地线大号侧'},
	{'value':'地线小号侧','label':'地线小号侧'}
];
var g_damper_flds = [
	{display: "类型", id: "type", newline: true,  type: "text", editor:{readonly:true}, group:'防振锤',  width:275},
	{display: "安装部位", id: "side", newline: true,  type: "select", editor: {data:g_damper_list}, group:'防振锤',  width:275},
	{display: "防振锤型号", id: "model", newline: true,  type: "text", group:'防振锤', width:275},
	{display: "防振锤数量", id: "count", newline: true,  type: "spinner", step:1, min:0,max:100, group:'防振锤', width:70, validate:{number: true}},
	{display: "安装距离", id: "distance", newline: false,  type: "spinner", step:0.1, min:0,max:100, group:'防振锤', width:80, validate:{number: true}},
	{display: "生产厂家", id: "manufacturer", newline: true,  type: "text", group:'防振锤', width:275},
	{display: "组装图号", id: "assembly_graph", newline: true,  type: "text", group:'防振锤', width:275}
];

var g_grd_flds = [
	{display: "类型", id: "type", newline: true,  type: "text", editor:{readonly:true}, group:'接地装置',  width:275},
	{display: "型号", id: "model", newline: true,  type: "text", group:'接地装置', width:275},
	{display: "数量", id: "count", newline: true,  type: "spinner", step:1, min:0,max:100, group:'接地装置', width:70, validate:{number: true}},
	{display: "埋深", id: "depth", newline: false,  type: "spinner", step:0.1, min:0.0,max:100.0, group:'接地装置', width:80, validate:{number: true}},
	{display: "生产厂家", id: "manufacturer", newline: true,  type: "text", group:'接地装置', width:275},
	{display: "组装图号", id: "assembly_graph", newline: true,  type: "text", group:'接地装置', width:275}
];

var g_platform_model_list = [
	{'value':'铁塔','label':'铁塔'},
	{'value':'水泥塔','label':'水泥塔'}
];
var g_base_flds_1 = [//基础
	{display: "类型", id: "type", newline: true,  type: "text", editor:{readonly:true}, group:'基础',  width:275},
	{display: "平台类型", id: "platform_model", newline: true,  type: "select", editor: {data:g_platform_model_list}, group:'基础', width:275},
	{display: "数量", id: "count", newline: true,  type: "spinner", step:1, min:0,max:100, group:'基础', width:70, validate:{number: true}},
	{display: "埋深", id: "depth", newline: false,  type: "spinner", step:0.1, min:0,max:100, group:'基础', width:80, validate:{number: true}},
	{display: "生产厂家", id: "manufacturer", newline: true,  type: "text", group:'基础', width:275},
	{display: "组装图号", id: "assembly_graph", newline: true,  type: "text", group:'基础', width:275}
];
var g_base_flds_2_3_4 = [//拉线  防鸟刺  在线监测装置
	{display: "类型", id: "type", newline: true,  type: "text", editor:{readonly:true}, group:'在线监测装置',  width:275},
	{display: "型号", id: "model", newline: true,  type: "text", group:'在线监测装置', width:275},
	{display: "数量", id: "count", newline: true,  type: "spinner", step:1, min:0,max:999, group:'在线监测装置', width:70, validate:{number: true}},
	{display: "生产厂家", id: "manufacturer", newline: true,  type: "text", group:'在线监测装置', width:275},
	{display: "组装图号", id: "assembly_graph", newline: true,  type: "text", group:'在线监测装置', width:275}
];
var g_base_flds_5 = [ //雷电计数器
	{display: "类型", id: "type", newline: true,  type: "text", editor:{readonly:true}, group:'雷电计数器',  width:275},
	{display: "型号", id: "model", newline: true,  type: "text", group:'雷电计数器', width:275},
	{display: "读数", id: "counter", newline: true,  type: "spinner", step:1, min:0,max:999, group:'雷电计数器', width:70, validate:{number: true}},
	{display: "生产厂家", id: "manufacturer", newline: true,  type: "text", group:'雷电计数器', width:275},
	{display: "组装图号", id: "assembly_graph", newline: true,  type: "text", group:'雷电计数器', width:275}
];


var g_tower_baseinfo_fields = [
	{ id: "id", type: "hidden" },
	//地理信息
	{ display: "经度", id: "lng", newline: true,  type: "geographic", group:'地理信息', width:300 , validate:{required:true, number: true}, 
		change:function( event, ui ) {
			var fid = $(event.target).attr('id');
			var id = $('#form_tower_info_base').webgisform('get', 'id').val();
			var viewer = $.viewer;
			var ellipsoid = viewer.scene.globe.ellipsoid;
			if(g_gltf_models[id])
			{
				if(event.currentTarget)
				{
					var lng = $('#form_tower_info_base').webgisform('get','lng').val(),
						lat = $('#form_tower_info_base').webgisform('get','lat').val(),
						height = $('#form_tower_info_base').webgisform('get','alt').val(),
						rotate = $('#form_tower_info_base').webgisform('get','rotate').val();
					if(!g_zaware) height = 0;
					lng = event.currentTarget.value;
					PositionModel(ellipsoid, g_gltf_models[id], lng, lat, height, rotate);
					var tower = GetTowerInfoByTowerId(id);
					if(tower)
					{
						RemoveSegmentsTower(viewer, tower);
						DrawSegmentsByTower(viewer, tower);
						RePositionPoint(viewer, id, lng, lat, height, rotate);
					}
				}
			}
			event.preventDefault();
		},
		spin:function( event, ui ) {
			var viewer = $.viewer;
			var ellipsoid = viewer.scene.globe.ellipsoid;
			var fid = $(event.target).attr('id');
			var id = $('#form_tower_info_base').webgisform('get','id').val();
			if(g_gltf_models[id])
			{
				var lng = $('#form_tower_info_base').webgisform('get','lng').val(),
					lat = $('#form_tower_info_base').webgisform('get','lat').val(),
					height = $('#form_tower_info_base').webgisform('get','alt').val(),
					rotate = $('#form_tower_info_base').webgisform('get','rotate').val();
				if(!g_zaware) height = 0;
				lng = ui.value;
				//RePositionPoint(viewer, id, lng, lat, height, rotate);
				PositionModel(ellipsoid, g_gltf_models[id], lng, lat, height, rotate);
			}
		}
	},
	{ display: "纬度", id: "lat", newline: true, type: "geographic",  group:'地理信息', width:300 , validate:{required:true, number: true},
		change:function( event, ui ) {
			var viewer = $.viewer;
			var ellipsoid = viewer.scene.globe.ellipsoid;
			var fid = $(event.target).attr('id');
			var id = $('#form_tower_info_base').webgisform('get','id').val();
			if(g_gltf_models[id])
			{
				if(event.currentTarget)
				{
					var lng = $('#form_tower_info_base').webgisform('get','lng').val(),
						lat = $('#form_tower_info_base').webgisform('get','lat').val(),
						height = $('#form_tower_info_base').webgisform('get','alt').val(),
						rotate = $('#form_tower_info_base').webgisform('get','rotate').val();
					if(!g_zaware) height = 0;
					lat = event.currentTarget.value;
					PositionModel(ellipsoid, g_gltf_models[id], lng, lat, height, rotate);
					var tower = GetTowerInfoByTowerId(id);
					if(tower)
					{
						RemoveSegmentsTower(viewer, tower);
						DrawSegmentsByTower(viewer, tower);
						RePositionPoint(viewer, id, lng, lat, height, rotate);
					}
				}
			}
			event.preventDefault();
		},
		spin:function( event, ui ) {
			var viewer = $.viewer;
			var ellipsoid = viewer.scene.globe.ellipsoid;
			var fid = $(event.target).attr('id');
			var id = $('#form_tower_info_base').webgisform('get','id').val();
			if(g_gltf_models[id])
			{
				var lng = $('#form_tower_info_base').webgisform('get','lng').val(),
					lat = $('#form_tower_info_base').webgisform('get','lat').val(),
					height = $('#form_tower_info_base').webgisform('get','alt').val(),
					rotate = $('#form_tower_info_base').webgisform('get','rotate').val();
				if(!g_zaware) height = 0;
				lat = ui.value;
				//RePositionPoint(viewer, id, lng, lat, height, rotate);
				PositionModel(ellipsoid, g_gltf_models[id], lng, lat, height, rotate);
			}
		}
	},
	{ display: "海拔(米)", id: "alt", newline: true, type: "spinner", step:0.5, min:0,max:9999, group:'地理信息', width:300 , validate:{required:true, number: true},
		change:function( event, ui ) {
			if(event.currentTarget)
			{
				var viewer = $.viewer;
				var ellipsoid = viewer.scene.globe.ellipsoid;
				var fid = $(event.target).attr('id');
				var id = $('#form_tower_info_base').webgisform('get','id').val();
				var lng = $('#form_tower_info_base').webgisform('get','lng').val(),
					lat = $('#form_tower_info_base').webgisform('get','lat').val(),
					height = $('#form_tower_info_base').webgisform('get','alt').val(),
					rotate = $('#form_tower_info_base').webgisform('get','rotate').val();
				if(!g_zaware) height = 0;
				if(g_gltf_models[id])
				{
					height = event.currentTarget.value;
					PositionModel(ellipsoid, g_gltf_models[id], lng, lat, height, rotate);
					var tower = GetTowerInfoByTowerId(id);
					if(tower)
					{
						RemoveSegmentsTower(viewer, tower);
						DrawSegmentsByTower(viewer, tower);
						RePositionPoint(viewer, id, lng, lat, height, rotate);
					}
				}
			}
			event.preventDefault();
		},
		spin:function( event, ui ) {
			var viewer = $.viewer;
			var ellipsoid = viewer.scene.globe.ellipsoid;
			var fid = $(event.target).attr('id');
			var id = $('#form_tower_info_base').webgisform('get','id').val();
			var lng = $('#form_tower_info_base').webgisform('get','lng').val(),
				lat = $('#form_tower_info_base').webgisform('get','lat').val(),
				height = $('#form_tower_info_base').webgisform('get','alt').val(),
				rotate = $('#form_tower_info_base').webgisform('get','rotate').val();
			if(!g_zaware) height = 0;
			if(g_gltf_models[id]) 
			{
				height = ui.value;
				//RePositionPoint(viewer, id, lng, lat, height, rotate);
				PositionModel(ellipsoid, g_gltf_models[id], lng, lat, height, rotate);	
			}
		},
		attach:'<img src=""/>',
		attachclick:null
	},
	{ display: "旋转角度", id: "rotate", newline: true, type: "spinner", step:0.5, min:-180,max:180, group:'地理信息', width:300 , validate:{required:true, number: true},
		change:function( event, ui ) {
			if(event.currentTarget)
			{
				var viewer = $.viewer;
				var ellipsoid = viewer.scene.globe.ellipsoid;
				var fid = $(event.target).attr('id');
				var id = $('#form_tower_info_base').webgisform('get','id').val();
				var lng = $('#form_tower_info_base').webgisform('get','lng').val(),
					lat = $('#form_tower_info_base').webgisform('get','lat').val(),
					height = $('#form_tower_info_base').webgisform('get','alt').val(),
					rotate = $('#form_tower_info_base').webgisform('get','rotate').val();
				if(!g_zaware) height = 0;
				if(g_gltf_models[id])
				{
					rotate = event.currentTarget.value;
					PositionModel(ellipsoid, g_gltf_models[id], lng, lat, height, rotate);
					var tower = GetTowerInfoByTowerId(id);
					if(tower)
					{
						RemoveSegmentsTower(viewer, tower);
						DrawSegmentsByTower(viewer, tower);
						RePositionPoint(viewer, id, lng, lat, height, rotate);
					}
				}
			}
			event.preventDefault();
		},
		spin:function( event, ui ) {
			var viewer = $.viewer;
			var ellipsoid = viewer.scene.globe.ellipsoid;
			var fid = $(event.target).attr('id');
			var id = $('#form_tower_info_base').webgisform('get','id').val();
			var lng = $('#form_tower_info_base').webgisform('get','lng').val(),
				lat = $('#form_tower_info_base').webgisform('get','lat').val(),
				height = $('#form_tower_info_base').webgisform('get','alt').val(),
				rotate = $('#form_tower_info_base').webgisform('get','rotate').val();
			if(!g_zaware) height = 0;
			if(g_gltf_models[id]) 
			{
				rotate = ui.value;
				//RePositionPoint(viewer, id, lng, lat, height, rotate);
				PositionModel(ellipsoid, g_gltf_models[id], lng, lat, height, rotate);	
			}
		}
	},
	//信息
	{ display: "名称", id: "tower_name", newline: true,  type: "text", group:'信息', width:330, validate:{required:true}},
	{ display: "代码", id: "tower_code", newline: true,  type: "text", group:'信息', width:330 },
	{ display: "塔型", id: "model_code", newline: true,  type: "text", group:'信息', width:100 },
	{ display: "呼称高", id: "denomi_height", newline: true,  type: "spinner", step:0.1, min:0,max:9999, group:'信息', width:90, validate:{number: true}},
	//电气
	{ display: "接地电阻", id: "grnd_resistance", newline: true,  type: "spinner", step:0.1, min:0,max:9999, group:'电气', width:300, validate:{number: true}},
	//土木
	{ display: "水平档距", id: "horizontal_span", newline: true,  type: "spinner", step:0.1, min:0,max:9999, group:'土木', width:85, validate:{number: true} },
	{ display: "垂直档距", id: "vertical_span", newline: true,  type: "spinner", step:0.1, min:0,max:9999, group:'土木', width:85, validate:{number: true} },
	//工程
	{ display: "所属工程", id: "project", newline: true,  type: "text", group:'工程', width:330 }
];

