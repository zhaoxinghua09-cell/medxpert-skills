# -*- coding: utf-8 -*-
"""Build medxpert-skills repo: copy skills, validate per agentskills.io spec, scan for sensitive strings, generate catalog."""
import os, re, shutil, json, sys

SRC = r"C:\Users\Administrator\.workbuddy\skills"
DST = r"D:\Workbuddy\2026-09-19-14-25-52\medxpert-skills"
SKILLS_DST = os.path.join(DST, "skills")
PATTERNS = [
    (r"[A-Za-z]:\\\\Users\\\\", "Windows user path"),
    (r"[A-Za-z]:/[Uu]sers/", "Windows user path"),
    (r"D:\\\\Workbuddy", "Local workspace path"),
    (r"D:/Workbuddy", "Local workspace path"),
    (r"@(qq|foxmail|gmail|163|outlook)\.com", "Email address"),
    (r"sk-[A-Za-z0-9]{16,}", "API key shape"),
    (r"(?i)api[_-]?key\s*[:=]", "api key field"),
    (r"(?i)(password|passwd|token)\s*[:=]\s*['\"]?[A-Za-z0-9]{8,}", "credential shape"),
    (r"AKID[A-Za-z0-9]+", "Tencent cloud key"),
    (r"zhaoxinghua", "Personal name/account"),
    (r"steven_hk25|xinghua06", "WeChat account"),
    (r"(?i)secret", "secret keyword"),
]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return None, text
    return m.group(1), text[m.end():]

def simple_yaml_get(fm, key):
    # crude: match "key: value" single-line (quoted or not)
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    if not m:
        return None
    v = m.group(1).strip()
    if v in ("|", ">", "|-", ">-"):
        return ""  # block scalar present
    return v.strip("'\"")

os.makedirs(SKILLS_DST, exist_ok=True)
results, catalog, excluded = [], [], []
dirs = sorted(d for d in os.listdir(SRC)
              if os.path.isdir(os.path.join(SRC, d))
              and re.match(r"^(medxpert-|medical-|med-reg-)", d))
for d in dirs:
    src_dir = os.path.join(SRC, d)
    sf = os.path.join(src_dir, "SKILL.md")
    if not os.path.isfile(sf):
        excluded.append((d, "no SKILL.md")); continue
    text = open(sf, encoding="utf-8", errors="replace").read()
    fm, _ = parse_frontmatter(text)
    issues = []
    if fm is None:
        issues.append("missing frontmatter"); name, desc = None, None
    else:
        name = simple_yaml_get(fm, "name"); desc = simple_yaml_get(fm, "description")
        if not name: issues.append("no name")
        elif not NAME_RE.match(name): issues.append("name not lowercase-hyphen")
        elif len(name) > 64: issues.append("name >64 chars")
        if not desc: issues.append("no single-line description (block scalar or missing)")
        elif len(desc) > 1024: issues.append("description >1024 chars")
    # sensitive scan over all text files in skill dir
    hits = set()
    for root, _, files in os.walk(src_dir):
        for fn in files:
            p = os.path.join(root, fn)
            if os.path.splitext(fn)[1].lower() in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".mp4", ".woff", ".ttf", ".bin", ".exe"): continue
            try: c = open(p, encoding="utf-8", errors="replace").read()
            except Exception: continue
            for pat, label in PATTERNS:
                if re.search(pat, c): hits.add(label)
    results.append((d, name, issues, sorted(hits)))

print(f"{'DIR':38} {'STATUS':6} ISSUES / SENSITIVE HITS")
publishable = 0
for d, name, issues, hits in results:
    ok = not issues and not hits
    if ok: publishable += 1
    print(f"{d:38} {'OK' if ok else 'CHECK':6} {issues if issues else ''}{' SENS:' + ','.join(hits) if hits else ''}")
print(f"\ntotal={len(results)} publishable={publishable}")

# copy all to repo regardless; exclusions applied manually at publish time
for d, name, issues, hits in results:
    src_dir = os.path.join(SRC, d)
    dst_dir = os.path.join(SKILLS_DST, d)
    if os.path.exists(dst_dir): shutil.rmtree(dst_dir)
    shutil.copytree(src_dir, dst_dir)
print("copied to", SKILLS_DST)
