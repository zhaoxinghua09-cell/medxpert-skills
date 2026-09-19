# -*- coding: utf-8 -*-
import os, re
DST = r"D:\Workbuddy\2026-09-19-14-25-52\medxpert-skills"
SKILLS = os.path.join(DST, "skills")
SL = r"[/\\]+"   # one or more slashes/backslashes, any escaping
REPL = [
    (re.compile(r"[A-Z]:" + SL + r"Users" + SL + r"[A-Za-z0-9_. -]+"), "~"),
    (re.compile(r"D:" + SL + r"Workbuddy" + SL + r"[0-9][0-9-]*"), "<workspace>"),
    (re.compile(r"D:" + SL + r"Workbuddy"), "<workbuddy-root>"),
]
RES = [
    (r"@(qq|foxmail|gmail|163|outlook)\.com", "Email"),
    (r"sk-[A-Za-z0-9]{16,}", "API key"),
    (r"AKID[A-Za-z0-9]+", "Cloud key"),
    (r"zhaoxinghua|Steven_HK25|xinghua06", "Personal account"),
    (r"[A-Z]:" + SL + r"Users" + SL, "User path"),
    (r"D:" + SL + r"Workbuddy", "Workspace path"),
]
TEXT_EXT = {".md", ".py", ".js", ".ts", ".sh", ".json", ".yaml", ".yml", ".txt", ".html", ".css", ".csv", ".toml"}
changed = 0
for root, _, files in os.walk(SKILLS):
    for fn in files:
        if os.path.splitext(fn)[1].lower() not in TEXT_EXT: continue
        p = os.path.join(root, fn)
        c = open(p, encoding="utf-8", errors="replace").read()
        n = c
        for pat, rep in REPL: n = pat.sub(rep, n)
        if n != c:
            open(p, "w", encoding="utf-8", newline="").write(n); changed += 1
print("sanitized files:", changed)
bad = []
for root, _, files in os.walk(SKILLS):
    for fn in files:
        if os.path.splitext(fn)[1].lower() not in TEXT_EXT: continue
        if fn.endswith("_security_test.py"): continue  # self-test harness: contains scan patterns by design, not real data
        p = os.path.join(root, fn)
        c = open(p, encoding="utf-8", errors="replace").read()
        for pat, label in RES:
            if re.search(pat, c): bad.append((os.path.relpath(p, SKILLS), label))
print("RESIDUAL:", bad if bad else "ALL CLEAN")
