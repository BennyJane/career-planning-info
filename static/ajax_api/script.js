$(document).ready(function () {
    // 初始化点赞状态
    function showLike(action = 'click') {
        $.get(`/like/click/${action}`, function (data, status) {
            if (status == "success") {
                if (data.likeStatus === 'false') {
                    $("#like-icon").attr("title", "求求你了，给个赞~~")
                    $("#like-icon a:nth-child(1)").hide()
                    $("#like-icon a:nth-child(2)").show()
                    $("#likeNum").text(data.likeSum + '人')
                } else {
                    $("#like-icon").attr("title", "谢谢你~~")
                    $("#like-icon a:nth-child(1)").show()
                    $("#like-icon a:nth-child(2)").hide()
                    $("#likeNum").text(data.likeSum + '人')
                }
            }
        })
    }

    showLike('browse')

    $("#like-icon").click(function () {
        showLike()
    })

    // 更新下载数量
    $(".download-num-asc").click(function () {
        let currentNum = $("#download-current-num").text()
        $("#download-current-num").text(parseInt(currentNum) + 1)
    })

});