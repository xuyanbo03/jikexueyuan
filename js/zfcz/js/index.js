(function go() {
    //input result
    var input = [];
    //character temp
    var tempChar = [];
    //appearTimes temp
    var tempTimes = [];

    //read input
    function read() {
        var read = document.getElementById("view").value;
        if (read == "") {
            //value initialize
            input = ["a", "x", "b", "d", "m", "a", "k", "m", "p", "j", "a"];
        } else {
            //如果重复提交则直接返回
            if (input == read) {
                return;
            }
            //将read转化为数据给input
            input = read.toLowerCase().concat();
            var temp = [];
            var char = 0;
            for (var i = 0; i < input.length; i++) {
                //截取字符串
                var char = input.substring(i, i + 1);
                //字符串传给temp数组
                temp.push(char);
            }
            //concat() 方法用于连接两个或多个数组
            input = temp.concat();
        }
    }

    //view devide by
    function view() {
        document.getElementById("view").value = input.join(" ");
    }

    //character找到互异的符号数组，并且得到他们出现的次数数组
    function character() {
        //数组复制
        var temp = input.concat();
        var char = 0;
        while (temp.length > 0) {
            //zidan
            tempChar.push(temp[0]);
            char = temp[0];
            //splice() 方法向/从数组中添加/删除项目，然后返回被删除的项目
            temp.splice(0, 1);
            //初始化并计数
            tempTimes.push("0");
            var j = tempTimes.pop();
            j = parseInt(j) + 1;
            tempTimes.push(j);
            //indexOf() 方法可返回某个指定的字符串值在字符串中首次出现的位置
            //如果剩下的有形同元素，则定位，之后打掉，并计数
            while (temp.indexOf(char) != -1) {
                temp.splice(temp.indexOf(char), 1);
                //计数
                var i = tempTimes.pop();
                i = parseInt(i) + 1;
                tempTimes.push(i);
            }
        }
    }

    function submit() {
        read();
        view();
        character();

        //得到做大值
        var maxNum = tempTimes[0];
        for (var i = 0; i < tempTimes.length; i++) {
            if (maxNum < tempTimes[i]) {
                maxNum = tempTimes[i];
            }
        }
        var position = tempTimes.indexOf(maxNum);

        //显示字符和出现次数
        document.getElementById("character").innerHTML = tempChar[position];
        document.getElementById("characterAppearNum").innerHTML = maxNum;

        //将查找符号的位置
        var order = [];
        for (var orderChar = 0; orderChar < input.length; orderChar++) {
            if (input[orderChar] == tempChar[position]) {
                order.push(orderChar);
            }
        }

        //显示次序
        document.getElementById("order").innerHTML = order;
        //清空结果
        tempTimes = [];
        tempChar = [];
    }

    //querySelector() 方法返回文档中匹配指定的选择器组的第一个元素(使用深度优先先序遍历文档的节点 | 并且通过文档标记中的第一个元素，并按照子节点数量的顺序迭代顺序节点)
    document.querySelector("#submit").onclick = submit;
})();