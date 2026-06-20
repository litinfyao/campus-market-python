# [组员B] 发布页完善：表单 + 图片上传 + 数据校验

## 任务分配：组员B

### 负责文件
- `templates/post.html`（主要）
- `data/categories.py`（辅助，已有骨架）

### 功能要求
1. **发布表单**：标题、描述、价格、分类、校区、成色、联系方式
2. **图片上传**：支持多图上传（前端预览）
3. **数据校验**：前端 + 后端双重校验
4. **提交成功**：跳转商品详情页

### 数据来源
- `categories.get_category_list()` 获取分类
- `categories.get_campus_list()` 获取校区
- `categories.get_condition_list()` 获取成色选项

### 验收标准
- [ ] 表单字段完整
- [ ] 图片能上传并预览
- [ ] 提交后有成功提示
- [ ] 后端校验防止空数据

### 完成后
提交 PR 到 `master` 分支，@litinfyao 审核。
