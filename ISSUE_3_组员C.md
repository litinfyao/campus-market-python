# [组员C] 详情页 + 登录逻辑完善

## 任务分配：组员C

### 负责文件
- `templates/detail.html`（主要）
- `data/users.py`（辅助）
- `data/page_text.py`（辅助）
- `app.py` 中的 `/login` 路由（与组长协作）

### 功能要求
1. **详情页**：商品完整信息、发布者信息、联系电话按钮
2. **登录页**：已经在 `login.html`，需要完善后端验证
3. **用户数据**：`users.py` 中补充更多模拟用户
4. **页面文案**：`page_text.py` 中补充各页面文案

### 数据来源
- `listings.get_listing_by_id(id)` 获取商品详情
- `users.get_user_by_id(uid)` 获取用户信息
- `users.validate_user(username, password)` 验证登录

### 验收标准
- [ ] 详情页展示完整
- [ ] 登录验证逻辑正确
- [ ] 登录后 session 正常
- [ ] 页面文案无错别字

### 完成后
提交 PR 到 `master` 分支，@litinfyao 审核。
