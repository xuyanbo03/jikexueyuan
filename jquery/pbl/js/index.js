//补充数据
var dataImg = { "data": [{ "src": "1.jpg" }, { "src": "2.jpg" }, { "src": "3.jpg" }, { "src": "4.jpg" }, { "src": "5.jpg" }, { "src": "6.jpg" }, { "src": "7.jpg" }, { "src": "8.jpg" }, { "src": "9.jpg" }, { "src": "10.jpg" }] };

$(document).ready(function() {
    $(window).on("load", function() {
        while (loadImgOrNot()) {
            createImg();
            imgLocation();
        }
        window.onscroll = function() {
            if (loadImgOrNot()) {
                createImg();
                imgLocation();
            }
        }
    });
});

//判断是否加载图片，返回true-false
function loadImgOrNot() {
    var windowHeight = $(window).innerHeight();
    var scrollTop = $(window).scrollTop();
    var lastImgBoxTop = $(".imgBox").last().position().top;
    var lastImgHeight = $(".imgBox").last().height();
    return (lastImgBoxTop < scrollTop + windowHeight) ? true : false;
}

// 批量添加图片
function createImg() {
    $.each(dataImg.data, function(index, value) {
        var imgBox = $("<div>").addClass("imgBox").appendTo($("#container"));
        var img = $("<div>").addClass("img").appendTo(imgBox);
        $("<img>").attr("src", "img/" + $(value).attr("src")).appendTo(img);
    });
}

//确定每个图片的位置
function imgLocation() {
    var box = $(".imgBox");
    var boxWidth = box.eq(0).width();
    var num = Math.floor($(window).width() / boxWidth);
    var boxArr = [];

    $("#container").css({ "width": (num * boxWidth) + "px" });
    box.each(function(index, value) {
        var boxHeight = box.eq(index).height();
        if (index < num) {
            boxArr[index] = boxHeight;
        } else {
            var minboxHeight = Math.min.apply(null, boxArr);
            var minboxIndex = $.inArray(minboxHeight, boxArr);
            $(value).css({
                "position": "absolute",
                "top": minboxHeight,
                "left": box.eq(minboxIndex).position().left
            });
            boxArr[minboxIndex] += box.eq(index).height();
        }
    });
}