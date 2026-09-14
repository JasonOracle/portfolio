# -*- coding: utf-8 -*-
"""整理作品集截图:按语义重命名并压缩为 WebP"""
import os, sys
sys.path.insert(0, r"C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\_site_pkgs")
from PIL import Image

CK = r"C:\Users\Administrator\.workbuddy\clipboard-images"
CKP = "clipboard-2026-09-13T17-07-57-"
WX = r"D:\soft\weixin\file\xwechat_files\wxid_ury2y1yc8zjq22_2e43\temp\RWTemp\2026-09\9e20f478899dc29eb19741386f9343c8"
OUT = r"D:\project\personal-site\portfolio\assets\img"
os.makedirs(OUT, exist_ok=True)

# (源文件, 目标名) 按用户给的项目顺序
MAP = [
    ("-496Z-21e4c24a.png", "aiwriter-1"), ("-499Z-544a2a81.png", "aiwriter-2"), ("-500Z-904dec48.png", "aiwriter-3"),
    ("-501Z-af517e74.png", "xuetang-1"), ("-503Z-abb11257.png", "xuetang-2"), ("-504Z-5a6056cc.png", "xuetang-3"),
    ("-505Z-8c262de4.png", "xuetang-4"), ("-506Z-31a0a1d1.png", "xuetang-5"),
    ("-507Z-c5c0ca5b.png", "jiayuan-1"),
    ("-508Z-78c86e60.png", "tbyy-1"), ("-509Z-2aee1be5.png", "tbyy-2"), ("-510Z-67b0358a.png", "tbyy-3"), ("-511Z-ce9262ce.png", "tbyy-4"),
    ("-512Z-70222747.png", "jiaozuoye-1"), ("-514Z-3cab469c.png", "jiaozuoye-2"), ("-515Z-6c9ce4be.png", "jiaozuoye-3"), ("-516Z-cd1a1405.png", "jiaozuoye-4"),
    ("-517Z-67ad282f.png", "ziliaoku-1"), ("-518Z-8e095286.png", "ziliaoku-2"), ("-519Z-b6bc735a.png", "ziliaoku-3"), ("-520Z-5e6ae615.png", "ziliaoku-4"),
    ("-520Z-bfb619ea.png", "cq-1"), ("-521Z-280ff857.png", "cq-2"), ("-522Z-870ca037.png", "cq-3"), ("-523Z-d9dc093c.png", "cq-4"),
    ("-524Z-ddcaacc4.png", "zuowen-1"), ("-525Z-d8ed7524.png", "zuowen-2"), ("-526Z-828aad55.png", "zuowen-3"), ("-527Z-6441952c.png", "zuowen-4"),
    ("-528Z-f34596ea.png", "yuwen-1"), ("-529Z-bca8b217.png", "yuwen-2"), ("-531Z-e4a454b0.png", "yuwen-3"), ("-533Z-6cb710a8.png", "yuwen-4"),
    ("-534Z-5fd6c149.png", "mbti-1"), ("-536Z-eba75ec8.png", "mbti-2"), ("-537Z-74382ea8.png", "mbti-3"), ("-538Z-7380e7d3.png", "mbti-4"),
    ("-539Z-727e463e.jpg", "jiari-web"), ("-540Z-d38220c1.png", "jiari-m-1"),
    ("-543Z-537f572f.png", "jrmall-1"), ("-545Z-5ba11b37.png", "jrmall-2"), ("-546Z-86f14128.png", "jrmall-3"),
    ("-548Z-e1b93427.png", "jrmall-4"), ("-549Z-3bd74332.png", "jrmall-5"),
    ("-551Z-e92af6e3.png", "jrrecruit-1"), ("-553Z-096e0eb8.png", "airesume-1"), ("-554Z-51357ea6.png", "xuetang-appstore"),
]
WXMAP = [("8b2aea223614f132e2ba84f85b72b405.jpg", "aiwriter-app-1"),
         ("4738d5bd6468c31a23b8cf5165bdfcbf.jpg", "aiwriter-app-2"),
         ("e66520a55825d1d57a9290cb1e01013e.jpg", "aiwriter-app-3")]

def convert(src, dst, max_w=460, q=80):
    im = Image.open(src)
    w, h = im.size
    if im.mode in ("RGBA", "P", "LA"):
        im = im.convert("RGBA")
    else:
        im = im.convert("RGB")
    if w > max_w:
        im = im.resize((max_w, int(h * max_w / w)), Image.LANCZOS)
    out = os.path.join(OUT, dst + ".webp")
    if dst == "jiari-web":  # 官网横图保留大宽度
        im = Image.open(src).convert("RGB")
        if im.size[0] > 900:
            im = im.resize((900, int(im.size[1] * 900 / im.size[0])), Image.LANCZOS)
    im.save(out, "WEBP", quality=q, method=6)
    return os.path.getsize(out), os.path.getsize(src)

total_out, total_in, n = 0, 0, 0
errs = []
for suffix, name in MAP + [(f, n2) for f, n2 in WXMAP]:
    if suffix in ("8b2aea223614f132e2ba84f85b72b405.jpg", "4738d5bd6468c31a23b8cf5165bdfcbf.jpg", "e66520a55825d1d57a9290cb1e01013e.jpg"):
        src = os.path.join(WX, suffix)
    else:
        src = os.path.join(CK, CKP + suffix.lstrip("-"))
    try:
        o, i = convert(src, name)
        total_out += o; total_in += i; n += 1
        print(f"ok {name}.webp  {i//1024}KB -> {o//1024}KB")
    except Exception as e:
        errs.append(f"{name}: {src} -> {e}")

print(f"\ndone {n} images, {total_in//1024}KB -> {total_out//1024}KB")
if errs:
    print("ERRORS:")
    for e in errs: print(" ", e)
