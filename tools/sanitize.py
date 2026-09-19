# -*- coding: utf-8 -*-
"""Sanitize skills in medxpert-skills/skills: mechanical replacements for local paths & personal accounts.
Internal-only skills moved to internal/ (gitignored). Re-scan afterwards."""
import os, re, shutil

DST = r"D:\Workbuddy\2026-09-19-14-25-52\medxpert-skills"
SKILLS = os.path.join(DST, "skills")
INTERNAL = os.path.join(DST, "internal")

# skills whose whole purpose is internal ops -> not for public repo
INTERNAL_ONLY = {
    "medxpert-cos-deploy", "medxpert-site-update", "medxpert-jiedan-loop",
    "medxpert-kb-intake", "medxpert-content-publish", "medxpert-content-ops",
    "medxpert-consult-port", "medxpert-reg-hub__skillhub",
}

REPLACEMENTS = [
    (re.compile(r"[A-Z]:\\Users\\Administrator"), "~"),
    (re.compile(r"[A-Z]:/Users/Administrator"), "~"),
    (re.compile(r"[A-Z]:\\\\Users\\\\Administrator"), "~"),
    (re.compile(r"[A-Z]:\\Users\\[A-Za-z0-9_ -]+"), "~"),
    (re.compile(r"[A-Z]:/Users/[A-Za-z0-9_ -]+"), "~"),
    (re.compile(r"D:\\\\Workbuddy\\\\[0-9-]+"), "<workspace>"),
    (re.compile(r"D:/Workbuddy/[0-9-]+"), "<workspace>"),
    (re.compile(r"D:\\\\Workbuddy"), "<workbuddy-root>"),
    (re.compile(r"D:/Workbuddy"), "<workbuddy-root>"),
    (re.compile(r"zhaoxinghua2022|zhaoxinghua06|zhaoxinghua"), "<account>"),
    (re.compile(r"Steven_HK25|xinghua06"), "<wechat-account>"),
]
# residual sensitive patterns for re-scan
RESIDUAL = [
    (r"@(qq|foxmail|gmail|163|outlook)\.com", "Email address"),
    (r"sk-[A-Za-z0-9]{16,}", "API key shape"),
    (r"(?i)api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9]{8,}", "api key value"),
    (r"(?i)(password|passwd)\s*[:=]\s*['\"]?[A-Za-z0-9]{8,}", "credential shape"),
    (r"AKID[A-Za-z0-9]+", "Tencent cloud key"),
    (r"zhaoxinghua|Steven_HK25|xinghua06", "Personal account"),
    (r"[A-Z]:\\+Users\\+|[A-Z]:/Users/", "Windows user path"),
    (r"D:[/\\]+W(or)?kbuddy", "Local workspace path"),
]
TEXT_EXT = {".md", ".py", ".js", ".ts", ".sh", ".json", ".yaml", ".yml", ".txt", ".html", ".css", ".csv", ".toml"}

os.makedirs(INTERNAL, exist_ok=True)
moved = []
for d in sorted(os.listdir(SKILLS)):
    if d in INTERNAL_ONLY:
        dest = os.path.join(INTERNAL, d)
        if os.path.exists(dest): shutil.rmtree(dest)
        shutil.move(os.path.join(SKILLS, d), dest)
        moved.append(d)
print("moved to internal/:", moved)

changed = scanned = 0
for root, _, files in os.walk(SKILLS):
    for fn in files:
        if os.path.splitext(fn)[1].lower() not in TEXT_EXT: continue
        p = os.path.join(root, fn); scanned += 1
        c = open(p, encoding="utf-8", errors="replace").read()
        n = c
        for pat, rep in REPLACEMENTS: n = pat.sub(rep, n)
        if n != c:
            open(p, "w", encoding="utf-8", newline="").write(n); changed += 1
print(f"scanned {scanned} text files, sanitized {changed}")

# re-scan residual
bad = []
for root, _, files in os.walk(SKILLS):
    for fn in files:
        if os.path.splitext(fn)[1].lower() not in TEXT_EXT: continue
        p = os.path.join(root, fn)
        c = open(p, encoding="utf-8", errors="replace").read()
        for pat, label in RESIDUAL:
            if re.search(pat, c): bad.append((os.path.relpath(p, SKILLS), label))
if bad:
    print("RESIDUAL FINDINGS:")
    for b in bad: print("  ", b)
else:
    print("RESCAN: ALL CLEAN")
print("public skills:", len(os.listdir(SKILLS)), "| internal:", len(os.listdir(INTERNAL)))
