# database-proj

1. action_book_detail 的 put_in_data 函数新增要填的版本号 version, 库存 stock, 单价 price 和封面 cover
2. home 界面调整第一列把 ISBN 换成封面，新增排序按键，和 manage 的逻辑一样，需要更改查询函数加入排序条件，以及实现 manage 一样的 refresh_sort 函数
3. home 界面添加历史订单按钮，需要填 action_user_order 文件
4. cart 界面调整第一列为勾选用空列，第二列放封面，之后是书目等原先的列往后顺延，空列勾选框和封面的插入方法和manage一样
5. 实现了用户信息界面那里的开通会员按钮，需要填一下放在 action_user_profile 最下面的 buy_vip 类
6. 详细查询修正，新增put_in_data 和 get_class2函数
7. 订单统计界面 action_m 里的 action_stat
8. 实现了用户信息界面的退出登录

