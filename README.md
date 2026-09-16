# Portfolio · JasonOracle

**简体中文** | [English](README.en.md)

9 年前端 · AI-Native 全栈的个人作品集。纯静态实现（HTML / CSS / 原生 JS），无构建步骤、无第三方依赖，响应式适配移动端。

**在线访问**：[https://portfolio-bwz.pages.dev](https://portfolio-bwz.pages.dev) · Cloudflare Pages

## 页面结构

| 文件 | 说明 |
|------|------|
| `index.html` | 主页面 — 浅色主题（冷钛白 + 大字排版，主色 `#0071e3`，稳重专业） |
| `copy.html` | 「近期项目」模块的样式试验稿（与 `copy.md` 配套，验证后已合入主页面，可删） |
| `assets/img/` | 全部 WebP 压缩截图，整站约 3MB |

## 内容模块

- **Hero + 数据条**：9 年经验 / 百万营收 / 10+ 款上架 / 2 套独立全栈
- **精选作品**：4 个重点案例（智题库三端 AI 测评 SaaS、倍进 AI 写作矩阵、烘焙连锁 App、AI 客服系统），左文右图不对称排布
- **近期项目**：AI 工程基建 ×4（agent-design-figma / CrossBrain / figma-agent-bridge / agent-bridge）
- **更多项目**：20+ 项目卡片墙（bento 网格，含 3 个千万级营收 / 百万级用户项目）
- **技能栈**：按「熟练 / 自学 / 暂无实战」诚实分层的五卡片布局

## 技术要点

- **零依赖**：原生 HTML / CSS / JS 单文件实现，无框架、无构建
- **图片灯箱**：点击看大图、多图左右切换（键盘 ←→ / 触屏滑动）、在线地址直达、多图角标提示
- **滚动浮现**：IntersectionObserver 驱动入场动画，并支持 `prefers-reduced-motion` 静态兜底
- **动效克制**：hover 只动 `transform` / `opacity`，GPU 友好

## 部署（Cloudflare Pages）

1. Cloudflare Dashboard → Workers & Pages → Create → Pages → Connect to Git
2. 选择本仓库，构建配置：
   - Framework preset: **None**
   - Build command: 留空
   - Build output directory: `/`
3. 部署完成后即可访问 `*.pages.dev` 域名，后续推送自动更新

---

📬 liuyn2017@qq.com · [GitHub 主页](https://github.com/JasonOracle)
