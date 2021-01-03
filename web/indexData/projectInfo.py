# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : ProjectStruct-3-simple
from collections import namedtuple
from web.utils.index import lastUpdate

"""
=======================================================================================================================
项目更新记录
=======================================================================================================================
"""

pencil_icon = """<svg xmlns="http://www.w3.org/2000/svg"
     width="24px" height="24px"
     viewBox="0 0 24 24" version="1.1">
    <g stroke="none" stroke-width="1"
       fill="none" fill-rule="evenodd">
        <rect x="0" y="0" width="24"
              height="24"/>
        <path d="M11.7573593,15.2426407 L8.75735931,15.2426407 C8.20507456,15.2426407 7.75735931,15.6903559 7.75735931,16.2426407 C7.75735931,16.7949254 8.20507456,17.2426407 8.75735931,17.2426407 L11.7573593,17.2426407 L11.7573593,18.2426407 C11.7573593,19.3472102 10.8619288,20.2426407 9.75735931,20.2426407 L5.75735931,20.2426407 C4.65278981,20.2426407 3.75735931,19.3472102 3.75735931,18.2426407 L3.75735931,14.2426407 C3.75735931,13.1380712 4.65278981,12.2426407 5.75735931,12.2426407 L9.75735931,12.2426407 C10.8619288,12.2426407 11.7573593,13.1380712 11.7573593,14.2426407 L11.7573593,15.2426407 Z"
              fill="#000000" opacity="0.3"
              transform="translate(7.757359, 16.242641) rotate(-45.000000) translate(-7.757359, -16.242641)"/>
        <path d="M12.2426407,8.75735931 L15.2426407,8.75735931 C15.7949254,8.75735931 16.2426407,8.30964406 16.2426407,7.75735931 C16.2426407,7.20507456 15.7949254,6.75735931 15.2426407,6.75735931 L12.2426407,6.75735931 L12.2426407,5.75735931 C12.2426407,4.65278981 13.1380712,3.75735931 14.2426407,3.75735931 L18.2426407,3.75735931 C19.3472102,3.75735931 20.2426407,4.65278981 20.2426407,5.75735931 L20.2426407,9.75735931 C20.2426407,10.8619288 19.3472102,11.7573593 18.2426407,11.7573593 L14.2426407,11.7573593 C13.1380712,11.7573593 12.2426407,10.8619288 12.2426407,9.75735931 L12.2426407,8.75735931 Z"
              fill="#000000"
              transform="translate(16.242641, 7.757359) rotate(-45.000000) translate(-16.242641, -7.757359)"/>
        <path d="M5.89339828,3.42893219 C6.44568303,3.42893219 6.89339828,3.87664744 6.89339828,4.42893219 L6.89339828,6.42893219 C6.89339828,6.98121694 6.44568303,7.42893219 5.89339828,7.42893219 C5.34111353,7.42893219 4.89339828,6.98121694 4.89339828,6.42893219 L4.89339828,4.42893219 C4.89339828,3.87664744 5.34111353,3.42893219 5.89339828,3.42893219 Z M11.4289322,5.13603897 C11.8194565,5.52656326 11.8194565,6.15972824 11.4289322,6.55025253 L10.0147186,7.96446609 C9.62419433,8.35499039 8.99102936,8.35499039 8.60050506,7.96446609 C8.20998077,7.5739418 8.20998077,6.94077682 8.60050506,6.55025253 L10.0147186,5.13603897 C10.4052429,4.74551468 11.0384079,4.74551468 11.4289322,5.13603897 Z M0.600505063,5.13603897 C0.991029355,4.74551468 1.62419433,4.74551468 2.01471863,5.13603897 L3.42893219,6.55025253 C3.81945648,6.94077682 3.81945648,7.5739418 3.42893219,7.96446609 C3.0384079,8.35499039 2.40524292,8.35499039 2.01471863,7.96446609 L0.600505063,6.55025253 C0.209980772,6.15972824 0.209980772,5.52656326 0.600505063,5.13603897 Z"
              fill="#000000" opacity="0.3"
              transform="translate(6.014719, 5.843146) rotate(-45.000000) translate(-6.014719, -5.843146)"/>
        <path d="M17.9142136,15.4497475 C18.4664983,15.4497475 18.9142136,15.8974627 18.9142136,16.4497475 L18.9142136,18.4497475 C18.9142136,19.0020322 18.4664983,19.4497475 17.9142136,19.4497475 C17.3619288,19.4497475 16.9142136,19.0020322 16.9142136,18.4497475 L16.9142136,16.4497475 C16.9142136,15.8974627 17.3619288,15.4497475 17.9142136,15.4497475 Z M23.4497475,17.1568542 C23.8402718,17.5473785 23.8402718,18.1805435 23.4497475,18.5710678 L22.0355339,19.9852814 C21.6450096,20.3758057 21.0118446,20.3758057 20.6213203,19.9852814 C20.2307961,19.5947571 20.2307961,18.9615921 20.6213203,18.5710678 L22.0355339,17.1568542 C22.4260582,16.76633 23.0592232,16.76633 23.4497475,17.1568542 Z M12.6213203,17.1568542 C13.0118446,16.76633 13.6450096,16.76633 14.0355339,17.1568542 L15.4497475,18.5710678 C15.8402718,18.9615921 15.8402718,19.5947571 15.4497475,19.9852814 C15.0592232,20.3758057 14.4260582,20.3758057 14.0355339,19.9852814 L12.6213203,18.5710678 C12.2307961,18.1805435 12.2307961,17.5473785 12.6213203,17.1568542 Z"
              fill="#000000" opacity="0.3"
              transform="translate(18.035534, 17.863961) scale(1, -1) rotate(45.000000) translate(-18.035534, -17.863961)"/>
    </g>
</svg>"""

start_icon = """<svg t="1605789889143" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
     p-id="12869" width="170" height="170">
    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <path d="M372.136585 449.560976c-9.990244 9.990244-9.990244 24.97561 0 34.965853 9.990244 9.990244 24.97561 9.990244 34.965854 0 32.468293-32.468293 87.414634-32.468293 119.882927 0 14.985366 14.985366 24.97561 37.463415 24.97561 59.941464 0 22.478049-9.990244 44.956098-24.97561 59.941463-32.468293 32.468293-87.414634 32.468293-119.882927 0-9.990244-9.990244-24.97561-9.990244-34.965854 0-9.990244 9.990244-9.990244 24.97561 0 34.965854 27.473171 27.473171 59.941463 39.960976 94.907317 39.960975s69.931707-12.487805 94.907318-39.960975c24.97561-24.97561 39.960976-59.941463 39.960975-94.907317S586.926829 474.536585 561.95122 449.560976c-49.95122-52.44878-137.365854-52.44878-189.814635 0zM756.760976 219.785366c-9.990244 9.990244-9.990244 24.97561 0 34.965854 12.487805 12.487805 17.482927 27.473171 17.482926 44.956097s-7.492683 32.468293-17.482926 44.956098c-24.97561 24.97561-64.936585 24.97561-89.912196 0-12.487805-12.487805-17.482927-27.473171-17.482926-44.956098s7.492683-32.468293 17.482926-44.956097c9.990244-9.990244 9.990244-24.97561 0-34.965854s-24.97561-9.990244-34.965853 0c-22.478049 22.478049-32.468293 49.95122-32.468293 79.921951 0 29.970732 12.487805 57.443902 32.468293 79.921951 22.478049 22.478049 49.95122 32.468293 79.921951 32.468293s57.443902-9.990244 79.921951-32.468293c22.478049-22.478049 32.468293-49.95122 32.468293-79.921951 0-29.970732-12.487805-57.443902-32.468293-79.921951-9.990244-9.990244-24.97561-9.990244-34.965853 0z"
              p-id="12870"
              fill="#000000"
              fill-rule="nonzero"/>
        <path d="M984.039024 99.902439c2.497561-19.980488-4.995122-39.960976-17.482926-52.44878-14.985366-14.985366-32.468293-22.478049-52.448781-22.478049-94.907317 4.995122-342.165854 42.458537-564.44878 264.741463-24.97561 24.97561-47.453659 49.95122-64.936586 72.429268L77.42439 399.609756c-27.473171 4.995122-49.95122 24.97561-57.443902 52.448781s-2.497561 54.946341 17.482927 74.926829l159.843902 159.843902c4.995122 4.995122 9.990244 4.995122 14.985366 7.492683 2.497561 4.995122 4.995122 7.492683 7.492683 12.487805-14.985366 2.497561-27.473171 9.990244-37.463415 19.980488-24.97561 24.97561-119.882927 192.312195-139.863414 227.278049-4.995122 9.990244-4.995122 22.478049 4.995122 29.970731 4.995122 4.995122 9.990244 7.492683 17.482926 7.492683 4.995122 0 7.492683 0 12.487805-2.497561 32.468293-19.980488 202.302439-114.887805 227.278049-139.863414 12.487805-12.487805 19.980488-27.473171 22.478049-42.458537 2.497561 0 4.995122 2.497561 7.492683 2.497561 0 7.492683 2.497561 14.985366 7.492683 19.980488l152.351219 152.351219c14.985366 14.985366 32.468293 22.478049 52.448781 22.478049 7.492683 0 14.985366 0 22.478048-2.497561 27.473171-7.492683 47.453659-29.970732 52.448781-57.443902l34.965854-202.302439v-9.990244c27.473171-22.478049 52.44878-44.956098 69.931707-62.439025 199.804878-209.795122 244.760976-467.043902 257.24878-569.443902zM72.429268 489.521951c-7.492683-7.492683-9.990244-14.985366-4.995122-24.97561 2.497561-7.492683 9.990244-14.985366 19.980488-14.985365l154.848781-27.473171c-27.473171 44.956098-44.956098 89.912195-52.448781 132.370732-2.497561 17.482927-2.497561 34.965854-2.497561 49.951219l-114.887805-114.887805z m202.302439 294.712195c0 9.990244-2.497561 17.482927-9.990244 24.97561-9.990244 9.990244-67.434146 44.956098-134.868292 84.917073 39.960976-67.434146 74.926829-124.878049 84.917073-134.868292 7.492683-7.492683 14.985366-9.990244 24.97561-9.990244 7.492683 0 12.487805 2.497561 17.482926 4.995122 2.497561 2.497561 7.492683 4.995122 9.990244 9.990244 4.995122 4.995122 7.492683 12.487805 7.492683 19.980487z m292.214634 144.858537c-2.497561 9.990244-7.492683 17.482927-17.482926 19.980488-9.990244 2.497561-17.482927 0-24.97561-4.995122L407.102439 824.195122h9.990244c62.439024 0 124.878049-27.473171 177.326829-59.941463l-27.473171 164.839024z m-262.243902-199.804878c-2.497561-2.497561-2.497561-4.995122-4.995122-4.995122-2.497561-2.497561-7.492683-4.995122-9.990244-7.492683-42.458537-44.956098-59.941463-94.907317-49.951219-154.84878 9.990244-72.429268 59.941463-152.35122 144.858536-237.268293 209.795122-209.795122 442.068293-244.760976 531.980488-249.756098 4.995122 0 9.990244 2.497561 12.487805 4.995122 2.497561 2.497561 4.995122 7.492683 4.995122 14.985366-9.990244 97.404878-54.946341 339.668293-247.258537 531.980488-149.853659 149.853659-284.721951 184.819512-382.126829 102.4z"
              p-id="12871"
              fill="#000000"
              fill-rule="nonzero"/>
    </g>
</svg>
"""

history = namedtuple('his', 'icon date info')

histories = [
    history(start_icon, "2020-10-28", "项目创建时间"),
    history(pencil_icon, "2020-11-19", "处理项目所需数据"),
    history(pencil_icon, "2020-11-21", "初步配置完首页数据"),
    history(pencil_icon, "2020-11-23", "完成表单数据展示"),
    history(pencil_icon, "2020-12-17", "完成线上部署"),
    history(pencil_icon, "2020-12-27", "更新docker-compose"),
    history(pencil_icon, "2021-01-01", "增加更多缓存设置，优化页面访问速度"),
]

lastInfo = lastUpdate(histories[-1].date)

end = [
    history(pencil_icon, lastInfo['date'], lastInfo['info']),
]

PROJECT_HISTORY = histories[-4:-1] + end
