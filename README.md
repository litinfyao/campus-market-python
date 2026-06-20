# 校园二手交易平台 · campus_market

> 第16周 Flask 小组协作项目

## 项目简介

本项目是一个简单的校园二手商品交易平台，基于 Flask 框架开发，支持商品浏览、分类筛选、详情查看、登录和发布商品等功能。

## 本地运行

```bash
pip install flask
python app.py
```

浏览器访问 http://127.0.0.1:5000

## 登录账号（测试用）

| 用户名     | 密码   |
|------------|--------|
| student01  | 123456 |
| student02  | abcdef |
| test       | test   |

## 项目分工

| 角色   | 分支名                   | 负责文件                                      |
|--------|--------------------------|-----------------------------------------------|
| 组长   | main                     | app.py / vercel.json / README.md / login.html |
| 组员 A | member-a-site-info       | data/site_info.py + templates/index.html      |
| 组员 B | member-b-categories      | data/categories.py + templates/post.html      |
| 组员 C | member-c-users-text      | data/users.py + data/page_text.py + templates/detail.html |
| 组员 D | member-d-listings-css    | data/listings.py + static/style.css           |

## 文件结构

```
campus_market/
├── app.py                # 组长：路由入口
├── requirements.txt      # flask
├── vercel.json           # 部署配置
├── README.md
├── data/
│   ├── __init__.py      # 空文件
│   ├── site_info.py      # 组员A
│   ├── categories.py     # 组员B
│   ├── users.py          # 组员C
│   ├── page_text.py      # 组员C
│   └── listings.py       # 组员D
├── templates/
│   ├── index.html        # 组员A
│   ├── post.html         # 组员B
│   ├── detail.html       # 组员C
│   └── login.html        # 组长
└── static/
    └── style.css         # 组员D
```

## 路由说明

| 路由 | 方法 | 功能 |
|------|------|------|
| / | GET | 首页，商品列表+筛选 |
| /detail/\<id\> | GET | 商品详情 |
| /post | GET+POST | 发布商品（需登录） |
| /login | GET+POST | 登录 |
| /logout | GET | 退出登录 |
