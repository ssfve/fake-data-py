import asyncio

from faker import Faker

from utils.mock_data import mock_data
from faker import Faker

from utils.mock_data import mock_data
from utils.db_utils import create_pool, run_async_task_in_loop, select_data
from utils.db_utils import insert_data

"""
This is a simple script to generate fake data for testing.
"""


async def batch_async_insert(pool):
    # create a insert sql for table fa_user
    # write show create table of table fa_user
    '''
            CREATE TABLE `fa_user` (
          `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
          `group_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '组别ID',
          `pid` int(10) DEFAULT '0' COMMENT '父id',
          `username` varchar(32) DEFAULT '' COMMENT '用户名',
          `nickname` varchar(50) DEFAULT '' COMMENT '昵称',
          `password` varchar(32) DEFAULT '' COMMENT '密码',
          `salt` varchar(30) DEFAULT '' COMMENT '密码盐',
          `email` varchar(100) DEFAULT '' COMMENT '电子邮箱',
          `mobile` varchar(11) DEFAULT '' COMMENT '手机号',
          
          `avatar` varchar(255) DEFAULT '' COMMENT '头像',
          
          `level` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '等级',
          `gender` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '性别',
          `birthday` date DEFAULT NULL COMMENT '生日',
          `bio` varchar(100) DEFAULT '' COMMENT '展示ID',
          `code` varchar(20) DEFAULT NULL COMMENT '邀请码',
          
          `money` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '余额',
          `score` int(10) NOT NULL DEFAULT '0' COMMENT '积分',
          `successions` int(10) unsigned NOT NULL DEFAULT '1' COMMENT '连续登录天数',
          `maxsuccessions` int(10) unsigned NOT NULL DEFAULT '1' COMMENT '最大连续登录天数',
          `prevtime` bigint(16) DEFAULT NULL COMMENT '上次登录时间',
          `logintime` bigint(16) DEFAULT NULL COMMENT '登录时间',
          `loginip` varchar(50) DEFAULT '' COMMENT '登录IP',
          `loginfailure` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '失败次数',
          `joinip` varchar(50) DEFAULT '' COMMENT '加入IP',
          `jointime` bigint(16) DEFAULT NULL COMMENT '加入时间',
          `createtime` bigint(16) DEFAULT NULL COMMENT '创建时间',
          `updatetime` bigint(16) DEFAULT NULL COMMENT '更新时间',
          `token` varchar(50) DEFAULT '' COMMENT 'Token',
          `status` varchar(30) DEFAULT '' COMMENT '状态',
          `verification` varchar(255) DEFAULT '' COMMENT '验证',
          `total` int(10) DEFAULT NULL COMMENT '累计充值',
          `openid` varchar(255) NOT NULL,
          `session_key` varchar(255) NOT NULL,
          PRIMARY KEY (`id`) USING BTREE,
          KEY `username` (`username`) USING BTREE,
          KEY `email` (`email`) USING BTREE,
          KEY `mobile` (`mobile`) USING BTREE
        ) ENGINE=InnoDB AUTO_INCREMENT=3399 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='会员表'
    '''
    # 188 1787 4376
    # 19 is fake
    prefix_sql = "insert INTO fa_user (group_id, pid, username, nickname, password, \
salt, email, mobile, avatar, level, \
gender, birthday, bio, code, money, \
score, successions, maxsuccessions, prevtime, logintime, \
loginip, loginfailure, joinip, jointime, createtime, \
updatetime, token, status, verification, total, \
openid, session_key) VALUES"

    value_str_list = []
    tasks = []
    # user_number = 62001
    user_number = 10
    # user_number = 11
    for i in range(1, user_number):
        value_str = mock_data(i)
        value_str_list.append(value_str)
        # python join list of str
        if i % 1 == 0:
            value_str = ",".join(value_str_list)
            # print(value_str)
            # this mysql connection pool is using system event loop
            # print(prefix_sql + value_str)
            # tasks.append(select_data(pool, "select {} from fa_user limit 1".format(i)))
            # tasks.append(yield print(prefix_sql + value_str))
            # yield prefix_sql + value_str
            # clear array
            value_str_list.clear()
            # print(i)
    # these tasks run separately
    await asyncio.gather(*tasks)


async def pool_execute():
    global pool
    host_name = "101.37.164.188"
    user_name = "playlet"
    user_password = "ysxFbnJt7TAECBw4"
    db_name = "playlet"

    # Create a connection
    loop = asyncio.get_event_loop()
    try:
        pool = await create_pool(loop, host_name, user_name, user_password, db_name)
        # pool is passed to batch_async_insert need to await
        await batch_async_insert(pool)
        # Commit after all inserts are successful
        # await pool.commit()
        # pool is autoCommit
    finally:
        pool.close()  # Close the pool async
        await pool.wait_closed()  # Wait for pool to close
        print("exited")
        # loop.run_until_complete();
        # The loop will close naturally when asyncio.run finishes
        # or if you're using another asyncio entry point
        # like `loop.run_until_complete()`

if __name__ == "__main__":
    # pool_execute()
    asyncio.run(pool_execute())
    #run_async_task_in_loop()
    # loop.run_
