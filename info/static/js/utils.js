function filter_status(status) {
    switch (status) {
        case 0:
            return "未执行"
        case 1:
            return "预执行"
        case 2:
            return "执行中"
        case 3:
            return "成功"
        case 4:
            return "失败"
        default:
            return "未执行"
    }
}