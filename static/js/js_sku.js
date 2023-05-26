/**init start */
//显示sku结构
function show_sku_item() {
	goodsName();
	SwiperData(info);
	productDetails();
	productImgInit();
	stockData(info);
	let price = document.getElementById('price');
		price.innerText = info.price;
	let market_price = document.getElementById('market_price');
		market_price.innerText = info.market_price;
	let agreement_price = document.getElementById('agreement_price');
		agreement_price.innerText = info.agreement_price;
	let sold_num = document.getElementById('sold_num');
		sold_num.innerText = info.sold_num;
	let stock = document.getElementById('stock');
		stock.innerText = stock_all;
	
	//sku选项部分
	var html = '';
	var option = info.skus_info;
	for(k in option) {
		sku_title = option[k].name;
		html += '<div class="goods_attr product_item" > <span class="label product_item_name">' + sku_title + '</span>';
		html += '<ul class="product_sku_item">';
		for(k2 in option[k].item) {
			sku_item = option[k].item[k2].name;
			html += '<li class="sku_item_li" name="sku_item" val="' + sku_item + '" >';
			html += '<span class="sku_name">' + sku_item + '</span>';
			html += '</li>';
		}
		html += '</ul>';
		html += '</div>';
	}
	$('#skuList').html(html);
	//	sku选项部分end
}

show_sku_item()

//模拟点击--是为了初始化就能将缺货的数据直接展示
setTimeout(function() {
	skuItemClick()
	skuItemClick()
}, 10);

/**init end */
//执行自动点击事件，这样就模拟出了自动执行点击事件
function skuItemClick(){
	var skuFirstData = info.skus_list[0].skus_param_array;
	var skuFirstParam =skuFirstData.split(',')
	var sku_li = document.getElementsByName("sku_item");
	for(i in sku_li){
		if (skuFirstParam[0] == sku_li[i].innerText) {
			//模拟鼠标点击
			simulateClick(i);
			break;
		}
	}
}
//模拟鼠标点击 数据中第一条sku属性的值info.skus_list[0].skus_param_array
function simulateClick(i) {
	var event = new MouseEvent('click', {
	    view: window,
	    bubbles: true,
	    cancelable: true
	});
	var cb = document.getElementsByClassName('sku_item_li')[i];  //whichever element you want to click
	var cancelled = !cb.dispatchEvent(event);
	if (cancelled) {
	    // A handler called preventDefault.
		//  alert("cancelled");
	} else {
	    // None of the handlers called preventDefault.
		//  alert("not cancelled");
	}
}
//产品标题
function goodsName(){
	var txt = info.goods_name;
	$("#goods_name").html(txt);
}
//首次产品图
function productImgInit(){
	var txt="";
		txt += '<img src="'+info.goods_imgs_array[0]+'" alt="">';
	$(".product_img").append(txt);
}
//求总库存
function stockData(info){
	var result = 0;
	for (var i = 0; i < info.skus_list.length; i++) {
		if(info.skus_list[i]!=null){
			result += parseInt(info.skus_list[i].stock);
		}
	}
	return stock_all=result;
}
//轮播图
function SwiperData(info){
	var txt="";
	for (var i = 0; i < info.goods_imgs_array.length; i++) {
		if(info.goods_imgs_array[i]!=null){
			txt += '<div class="swiper-slide"'+'>';
			txt += '<img src="'+info.goods_imgs_array[i]+'" alt="">';
			txt += '</div>';				
		}
	}
	$(".swiper-wrapper").append(txt);
}
//商品详情
function productDetails(){
	var txt="";
	txt += '<div class="product_details" >' + info.goods_details + '</div>';
	$("#goods_details").append(txt);
}

//sku
var sku_list = info.skus_list;

//获取所有包含指定节点的路线
function filterProduct(ids) {
	var result = [];
	$(sku_list).each(function(k, v) {
		_attr = ',' + v['skus_param_array'] + ',';
		_all_ids_in = true;
		for(k in ids) {
			if(_attr.indexOf(',' + ids[k] + ',') == -1) {
				_all_ids_in = false;
				break;
			}
		}
		if(_all_ids_in) {
			result.push(v);
		}
	});
	return result;
}
//获取 经过已选节点 所有线路上的全部节点
// 根据已经选择得属性值，得到余下还能选择的属性值
function filterAttrs(ids) {
	var products = filterProduct(ids);
//	console.log("products",products);
	var result = [];
	$(products).each(function(k, v) {
//		console.log("v",v)
		if(v.stock != 0 ){
			result = result.concat(v['skus_param_array'].split(','));
		}
	});
	return result;
}
//已选择的节点数组
//var activeSku = '';
function _getSelAttrId() {
	var list = [];
	$('.goods_attr li.productActive').each(function() {
		list.push($(this).attr('val'));
	});
	for(k in sku_list) {
		var arrJoinString =list.toString();
		sku_array = sku_list[k].skus_param_array;
		
		if(arrJoinString == sku_array){
			var activeSku = sku_list[k];
		}
		
	};
	
//	console.log("activeSku",activeSku)
	if(activeSku != undefined){
		//当条件都选上了调用显示函数
		show_data(activeSku);
	}
	
	return list;
}
$('.goods_attr li').click(function() {
	if($(this).hasClass('noneActive')) {
		return; //被锁定了,不可点
	}
	if($(this).hasClass('productActive')) {
		$(this).removeClass('productActive');
	} else {
		$(this).siblings().removeClass('productActive');
		$(this).addClass('productActive');
	}
	var select_ids = _getSelAttrId();
	//已经选择了的规格
	var $_sel_goods_attr = $('li.productActive').parents('.goods_attr');
	// step 1
	var all_ids = filterAttrs(select_ids);
	//获取未选择的
	var $other_notsel_attr = $('.goods_attr').not($_sel_goods_attr);
	//设置为选择属性中的不可选节点
	$other_notsel_attr.each(function() {
		set_block($(this), all_ids);
	});
	//step 2
	//设置已选节点的同级节点是否可选
	$_sel_goods_attr.each(function() {
		update_2($(this));
	});
});



function update_2($goods_attr) {
	// 若该属性值 $li 是未选中状态的话，设置同级的其他属性是否可选
	var select_ids = _getSelAttrId();
	var $li = $goods_attr.find('li.productActive');
	var select_ids2 = del_array_val(select_ids, $li.attr('val'));
	var all_ids = filterAttrs(select_ids2);
	set_block($goods_attr, all_ids);
}

function set_block($goods_attr, all_ids) {
	//根据 $goods_attr下的所有节点是否在可选节点中（all_ids） 来设置可选状态
	$goods_attr.find('li').each(function(k2, li2) {
		if($.inArray($(li2).attr('val'), all_ids) == -1) {
			$(li2).addClass('noneActive');
		} else {
			$(li2).removeClass('noneActive');
		}
	});
}

function del_array_val(arr, val) {
	//去除 数组 arr中的 val ，返回一个新数组
	var a = [];
	for(k in arr) {
		if(arr[k] != val) {
			a.push(arr[k]);
		}
	}
	return a;
}

//显示选中数据
function show_data(activeSku) {
//	console.log("activeSku:",activeSku)
	let price = document.getElementById('price');
		price.innerText = activeSku.price;
	let market_price = document.getElementById('market_price');
		market_price.innerText = activeSku.market_price;
	let agreement_price = document.getElementById('agreement_price');
		agreement_price.innerText = activeSku.agreement_price;
	let sold_num = document.getElementById('sold_num');
		sold_num.innerText = activeSku.sold_num;
	let stock = document.getElementById('stock');
		stock.innerText = activeSku.stock;
	productImg(activeSku.img);
}
//选中项图片
function productImg(product_img){
	var txt="";
		txt += '<img class="product_chooce_img" src="'+product_img+'" alt="">';
	$('.product_img .product_chooce_img').remove();
	$(".product_img").append(txt);
}
//sku_end

//Swiper
var galleryThumbs = new Swiper('.gallery_thumbs', {
	spaceBetween: 4,
	slidesPerView: 5,
	watchSlidesVisibility: true, //防止不可点击
	autoScrollOffset: 1,
})
var galleryTop = new Swiper('.gallery_top', {
	slidesPerView: 1,
	centeredSlides: true,
	loop: true,
	autoplay: {
		// 设置为false，用户操作之后自动切换不会停止，每次都会重新启动autoplay。
	    disableOnInteraction: false,
	},
	navigation: {
		nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev',
	},
	thumbs: {
		swiper: galleryThumbs,
	}
})