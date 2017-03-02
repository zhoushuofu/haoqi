;(function(window){
	
	function _$(id){
		return document.getElementById(id)
	}

	// 获取上传图片的表单
	// 门店头像
	var shopAvatar = _$('shopAvatar')
	// 门店头像按钮
	var shopAvatarBtn = _$('shopAvatarBtn')
	// 门店照片
	var shopImg = _$('shopImg')
	// 门店照片按钮
	var shopImgBtn = _$('shopImgBtn')
	
	// 自定义按钮模拟input点击
	shopAvatarBtn.onclick = function() {
		shopAvatar.click()
	}

	shopImgBtn.onclick = function() {	
		shopImg.click()
	}



})(window)