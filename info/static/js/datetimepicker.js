window.onload = function () {
    document.getElementById('datetimepicker').datetimepicker({
            format:'yyyy-mm-dd',
            startView: "year", //初始化视图是‘年’
            minView: "month",//最精确视图为'月'
            maxView: "decade"//最高视图为'十年'
        });
}