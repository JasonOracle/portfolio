# Portfolio · 刘亚楠（JasonOracle）

9 年前端 · AI-Native 全栈的个人作品集。纯静态实现（HTML / CSS / 原生 JS），无构建步骤，响应式适配移动端。

**在线访问**：[https://portfolio-bwz.pages.dev](https://portfolio-bwz.pages.dev) · Cloudflare Pages

## 页面结构

| 文件 | 说明 |
|------|------|
| `index.html` | 唯一版本 — 浅色主题（冷钛白 + 大字排版，稳重专业） |

## 内容

- 3 个重点作品（tiku 三端 AI 测评 SaaS / aiservice 智能客服 / 中焙智能 App）+ 20+ 项目卡片墙
- 全站图片灯箱：点击看大图、多图左右切换（键盘 ←→ / 触屏滑动）、在线地址直达
- 图片全部 WebP 压缩，整站约 3MB

## 部署（Cloudflare Pages）

1. Cloudflare Dashboard → Workers & Pages → Create → Pages → Connect to Git
2. 选择本仓库，构建配置：
   - Framework preset: **None**
   - Build command: 留空
   - Build output directory: `/`
3. 部署完成后即可访问 `*.pages.dev` 域名，后续推送自动更新

---

📬 liuyn2017@qq.com · [GitHub 主页](https://github.com/JasonOracle)
