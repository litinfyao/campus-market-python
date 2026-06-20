# 如何创建 4 个 Issue（2 分钟搞定）

## 方法一：网页复制粘贴（最快）

1. 打开：https://github.com/litinfyao/campus-market-python/issues/new
2. 复制下面每个 `.md` 文件的内容，粘贴到 GitHub Issue 创建页面
3. 点 "Submit new issue"

### 4 个 Issue 文件（都在项目根目录）：
- `ISSUE_1_组员A.md` → 复制标题 + 内容
- `ISSUE_2_组员B.md` → 复制标题 + 内容
- `ISSUE_3_组员C.md` → 复制标题 + 内容
- `ISSUE_4_组员D.md` → 复制标题 + 内容

---

## 方法二：用 GitHub CLI（需要先安装）

```bash
# 安装 gh CLI
# Windows: winget install GitHub.cli

# 登录
gh auth login

# 一键创建 4 个 Issue
gh issue create --repo litinfyao/campus-market-python --title "[组员A] 首页完善" --body-file ISSUE_1_组员A.md
gh issue create --repo litinfyao/campus-market-python --title "[组员B] 发布页完善" --body-file ISSUE_2_组员B.md
gh issue create --repo litinfyao/campus-market-python --title "[组员C] 详情页完善" --body-file ISSUE_3_组员C.md
gh issue create --repo litinfyao/campus-market-python --title "[组员D] CSS美化" --body-file ISSUE_4_组员D.md
```

---

## 完成后

记得把 Issue 链接发给对应组员，让他们知道自己要做什么！

## 查看所有 Issue
https://github.com/litinfyao/campus-market-python/issues
