# 📋 晚上操作清单（Steven 专用 · 10 分钟搞定）

## 第一步：重新登录 GitHub（1 分钟）

gh 的登录态过期了。在终端跑：

```
gh auth login -h github.com
```

按提示浏览器登录即可（凭据只进系统，不进对话）。

## 第二步：推送仓库（1 分钟，仓库已本地提交好）

```
cd D:\Workbuddy\2026-09-19-14-25-52\medxpert-skills
gh repo create medxpert-skills --public --source . --push
```

推完即上线：https://github.com/<你的用户名>/medxpert-skills
（如果想用 MedXpert 组织账号发，把上面 repo 名改成 `MedXpert/medxpert-skills`，前提是账号有组织权限）

## 第三步：扣子技能商店（可选，逐个上传，5 分钟）

1. 打开扣子 coze.cn → 技能商店 → 创建技能 → 导入技能包
2. 用 `medxpert-skills\zips\` 里的现成 zip（21 个，每个 SKILL.md 都在包根目录，直接能传）
3. 建议先传流量款：`medical-device-reg-hub`、`medical-device-qms-gmp`、`medical-device-compliance-grader`

## 已完成（不用你管）

- ✅ 21 个公开技能脱敏完毕，敏感扫描 3 轮全绿
- ✅ 8 个纯内部运维技能隔离到 `internal/`（gitignore，不会上 GitHub）
- ✅ AI 可发现性骨架：AGENTS.md + llms.txt + .nojekyll（按 ai-discoverability-skeleton 技能标准）
- ✅ README 中英双语 + 各客户端安装表
- ✅ git 已提交（e313fdf），`gh repo create --push` 一条命令即上线

## 注意

- 以后技能有更新：重跑 `tools/build_repo.py` → `tools/sanitize_pass2.py` → `tools/gen_skeleton.py`，再 commit + push
- 仓库地址定下来后，把 `AGENTS.md` / `llms.txt` / `README.md` 里的 `https://github.com/MedXpert/medxpert-skills` 替换成实际地址（跑一遍 `tools/gen_skeleton.py` 前改 `REPO_URL` 变量即可）
