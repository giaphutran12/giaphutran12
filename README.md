# Hey, I'm Edward 👋

**AI Engineer who ships.** Not "I watched a tutorial" ships. Production apps, real users, actual problems solved.

I build AI-powered products that people use. Led 8 interns to 2nd place at ISSP Expo 2025. Currently shipping at [Build Launch Iterate](https://buildlaunchiterate.ca).

---

## 🔥 What I've Built

### [Stolk](https://stocktwits-clone-2.vercel.app/) — Twitter for Stocks
> Save 10+ hours/week crawling through news. Get AI-powered sentiment analysis instead.

Real-time community sentiment aggregation with Claude AI analyzing quality posts, extracting themes, and summarizing discussions. News sentiment from 200+ articles across 20+ trusted sources.

**The flex:** `<1s latency` | `$0.001/analysis` | `64% improved sentiment accuracy`

`Next.js 16` `React 19` `Claude AI` `Prisma` `Neon PostgreSQL` `Inngest` `Clerk`

[Live Demo](https://stocktwits-clone-2.vercel.app/) • [YouTube Demo](https://youtu.be/RAuHtLJ9Mco)

---

### [X Recommendation Algorithm](https://github.com/giaphutran12/x-recommendation-algo) — Twitter's Ranking Pipeline, Rebuilt
> 50K tweets. 338K engagements. Two-Tower neural network. Your personalized feed in milliseconds.

TypeScript reimplementation of X/Twitter's recommendation algorithm. 5-stage ranking pipeline (retrieval → hydration → filtering → scoring → selection) with a Two-Tower neural network trained on 676K samples, exported to ONNX for TypeScript inference. 10 filters, 4 scorers, author diversity enforcement, and user-tunable algorithm weights. Trains in Python, runs in the browser.

**The flex:** `676K training samples` | `3.6KB ONNX model` | `50K→50 tweet ranking` | `6 engagement predictions`

`Next.js 16` `React 19` `Supabase` `PyTorch` `ONNX Runtime` `Tailwind CSS` `Vitest`

[GitHub](https://github.com/giaphutran12/x-recommendation-algo)

---

### [Self-Improving Prompt](https://github.com/giaphutran12/self-improving-prompt) — AI Prompt Engineering Toolkit
> Define prompts, test them, let AI agents analyze failures and improve automatically.

Multi-agent system that creates a feedback loop: define prompts → evaluate against test cases → AI analyzes failures → generates improved versions → repeat until 90% success rate. Converts user feedback into synthetic test cases to prevent recurring issues. Full-stack with separate FastAPI backend (async SQLAlchemy, Redis workers) and Next.js frontend.

`Next.js 16` `FastAPI` `PostgreSQL` `Redis` `Google Gemini` `SQLAlchemy`

[GitHub](https://github.com/giaphutran12/self-improving-prompt)

---

### [KID-WATCH](https://github.com/giaphutran12/kid-watch) — AI Study Monitor
> Real-time posture, phone, and gaze detection scored into student engagement metrics.

Production proof-of-concept for Viettel's 700,000 home camera deployment. Combines three computer vision models (MediaPipe Pose, MediaPipe Face, YOLOv8) into a weighted engagement score (0-100%) running at 20-30 FPS. Intelligent temporal smoothing, aspect ratio filtering, confidence thresholds, and session reports with personalized recommendations. Single-file Python app, fully offline, zero cloud dependencies.

**The flex:** `700k camera deployment target` | `3 ML models in real-time` | `20-30 FPS`

`Python` `OpenCV` `MediaPipe` `YOLOv8` `NumPy`

[GitHub](https://github.com/giaphutran12/kid-watch)

---

### BP Portal — Enterprise Mortgage Management
> AI-powered deal management system for a Canadian mortgage brokerage. 27 staff, 50+ brokers.

289-commit enterprise platform that syncs CRM data, generates proposal PDFs, and analyzes borrower credit profiles using Google Cloud Vertex AI. Background job processing with Inngest handles 5-13MB PDF extraction pipelines. Multi-zone deployment architecture with real-time data synchronization and enterprise-grade infrastructure (SOC 1/2/3, ISO 27001).

**The flex:** `289 commits` | `AI credit analysis` | `multi-zone deployment` | `real-time CRM sync`

`Next.js 16` `React 19` `Supabase` `Inngest` `Google Vertex AI` `Prisma` `Claude API`

*Internal tool — restricted access*

---

### [Vibe](https://vibe-psy.vercel.app/) — AI Website Builder
> Describe what you want. Get a full application. Yes, actually.

Multi-agent AI system that generates production-ready React apps from natural language. Sandboxed E2B environments for safe code execution. Ships complete TypeScript + Tailwind applications.

*"What, you really believe that? AI? Generating production-ready code?"* — Try it yourself.

`Next.js 15` `tRPC` `E2B Sandbox` `Claude 3.5` `Inngest Agent Kit` `Prisma`

[Live Demo](https://vibe-psy.vercel.app/) • [YouTube Demo](https://youtu.be/jlkZwwPMHps)

---

### PortPal — Shift Tracking for Port Workers
> Mobile-first PWA for ILWU longshoremen to log shifts, track earnings, and hit income goals.

Production Progressive Web App with 6 shift entry types, real-time earnings dashboard, goal tracking, and analytics. Full authentication system with Supabase, Stripe payment integration, and offline support for use at the port.

`Next.js 16` `React 19` `Supabase` `Stripe` `Tailwind CSS` `shadcn/ui`

*Private — client project*

---

### [AI Customer Support Agent](https://youtu.be/pnrKh72DNo8)
> Voice-enabled AI that actually knows your company's stuff.

RAG pipeline with Pinecone vector search (3072D embeddings), Firecrawl for auto-scraping company docs, and Vapi.ai for real-time voice conversations. <2s response time.

`Pinecone` `Google Gemini` `Vapi.ai` `Firecrawl` `Next.js 15`

[YouTube Demo](https://youtu.be/pnrKh72DNo8)

---

### [LLM Router](https://llm-router-mauve.vercel.app/) — Smart AI Model Selection
> Stop overpaying for simple prompts. Route to the right model automatically.

Analyzes your message intent and routes to the optimal model. Simple chat → free model. Coding → Claude. Complex reasoning → GPT-5. ~100ms routing overhead.

`Next.js 14` `TypeScript` `OpenRouter API`

[Live Demo](https://llm-router-mauve.vercel.app/) • [YouTube Demo](https://youtu.be/Kw9wHT2L9EM)

---

### [Portfolio](https://edwardtran.ca) — Personal Site
> 3D WebGL effects, buttery smooth scroll, Sanity CMS — built on darkroom.engineering's Satūs framework.

Custom portfolio with Three.js noise wave effects, GSAP + Framer Motion animations, and Lenis smooth scrolling. Content managed through Sanity CMS so I never touch the code to update projects. Built with Bun, strict TypeScript, and Biome for formatting.

`Next.js 16` `React 19` `Three.js` `GSAP` `Framer Motion` `Sanity CMS` `Tailwind CSS`

[Live Site](https://edwardtran.ca) • [GitHub](https://github.com/giaphutran12/portfolio)

---

### [Viet Bike Scout](https://viet-bike-scout.vercel.app/) — Vietnam Motorbike Price Comparison
> Compare rental prices across 18 shops in 4 cities. Parallel browser agents scrape them all simultaneously.

Fires TinyFish browser agents at 18+ rental websites across HCMC, Hanoi, Da Nang, and Nha Trang in parallel. Results stream back via SSE as each shop finishes — typically 15–30 seconds for a full city. Live iframe previews show each agent working in real time. 6-hour cache with graceful degradation.

**The flex:** `18 shops` | `4 cities` | `parallel browser agents` | `SSE streaming`

`Next.js 16` `React 19` `TinyFish` `Supabase` `Tailwind CSS` `shadcn/ui`

[Live Demo](https://viet-bike-scout.vercel.app/) • [GitHub](https://github.com/giaphutran12/viet-bike-scout)

---

### [Clinic Book](https://github.com/giaphutran12/clinic-book) — Healthcare Appointment Scraper
> Find available physio, massage, and chiro appointments across Vancouver in one search.

Scrapes clinic availability across Vancouver, North Vancouver, Burnaby, and Surrey. Server-sent events stream results as each clinic responds. Filter by practitioner type, get direct booking links.

`Next.js 16` `React 19` `TypeScript` `Tailwind CSS` `SSE`

[GitHub](https://github.com/giaphutran12/clinic-book)

---

### [Image Style Transfer](https://webassembly-image-transfer.vercel.app/) — WebGPU + Rust + ONNX
> Upload an image. Pick an art style. Watch Rust + WebAssembly transform it in your browser.

5 ONNX neural style transfer models (Udnie, Candy, Mosaic, Rain Princess, Pointilism) plus an Adversarial Inception v3 classifier — all running client-side via Rust compiled to WebAssembly. Zero server, zero cloud, zero latency.

**The flex:** `6 ML models` | `100% client-side` | `Rust → WASM` | `zero cloud dependency`

`Next.js 14` `React 18` `Rust` `WebAssembly` `ONNX` `Tailwind CSS`

[Live Demo](https://webassembly-image-transfer.vercel.app/) • [GitHub](https://github.com/giaphutran12/webassemby-rust-image-style-transfer)

---

### [Autoresearch](https://github.com/giaphutran12/autoresearch-macos) — Autonomous AI Research Agent
> Fork of Karpathy's autoresearch. AI agent modifies a GPT training script, trains for 5 min, keeps or discards, repeats overnight.

Ran Karpathy's autonomous research framework on Apple Silicon (M-series Mac with MPS). The agent ran 22 experiments overnight — modifying architecture, hyperparameters, batch size, and optimizer settings. Best result: **24.5% improvement** over baseline (val_bpb 1.924 → 1.453). Key findings: halving batch size from 65K→16K gave the biggest single win (−7.0%), optimal depth was 3 layers at 10.7M params, and learning rate tuning (MATRIX_LR 0.06) squeezed out the final gains.

**The flex:** `22 experiments overnight` | `24.5% val_bpb improvement` | `10.7M param model` | `Apple Silicon MPS`

`Python` `PyTorch` `MPS (Metal)` `Claude Agents`

[GitHub](https://github.com/giaphutran12/autoresearch-macos)

---

### Velocity — Real Estate Deal Management
> Deal tracking, appraiser network, and AI-powered analytics for a real estate brokerage.

Full-stack platform with deal pipeline management, appraiser directory with FSA postal code search and Leaflet map clustering, role-based access control, and multi-LLM integration (Claude, AWS Bedrock, Google Gemini). Background job processing with Inngest, PDF report generation, and real-time analytics dashboards.

`Next.js 16` `React 19` `Supabase` `Leaflet` `Inngest` `Claude API` `AWS Bedrock` `Google Gemini`

*Private — client project*

---

### Kolm Dashboard — Sauna Studio Business Intelligence
> Customer analytics, revenue tracking, and operational insights for Kolm Kontrast sauna studio.

Multi-section BI dashboard with customer funnels (Nivo), revenue metrics, operational reports, and data preprocessing pipelines. CSV import scripts normalize raw business data into Supabase. Advanced table views with TanStack React Table.

`Next.js 16` `React 19` `Supabase` `Nivo` `TanStack React Table` `Tailwind CSS`

*Private — client project*

---

### [Blue Pearl Landing Page](https://blue-pearl-landing-page.vercel.app/) — Mortgage Marketing Site
> Full marketing site for Blue Pearl Mortgages — debt calculator, Google testimonials, SEO, and lead gen.

Multi-page marketing site with interactive debt calculator, Google Maps integration, testimonial aggregation, blog, and lead capture. SEO-optimized with sitemaps, OG images, Google Ads tracking, and GTM. Email notifications via Resend.

`Next.js 16` `React 19` `Supabase` `Chart.js` `Google Maps` `Resend` `Vercel Analytics`

[Live Site](https://blue-pearl-landing-page.vercel.app/)

---

### [Call Analysis](https://github.com/giaphutran12/claude-call-analysis) — AI Call Intelligence Platform
> The app I built with 8 BCIT interns. AI-powered call analytics for sales teams.

Broker command center with call recording analysis, prospecting pipeline, booking management, and team competition dashboards. Normalized a nightmare dataset (200 rows × 220K columns of 10-year manual entries) into clean, queryable data. AI-powered insights surface patterns in sales calls.

**The flex:** `8 interns led` | `2nd place ISSP Expo 2025` | `<10ms queries` | `220K→clean columns`

`Next.js 15` `React 19` `TypeScript` `Recharts` `shadcn/ui` `Tailwind CSS`

[GitHub](https://github.com/giaphutran12/claude-call-analysis)

---

### [Whiteboard](https://github.com/giaphutran12/Whiteboard) — Douglas College IT Shift Tracker
> Live shift-tracking web app for Douglas College's IT department. Used daily by the service desk.

Employee management, shift scheduling, and contact directory with real-time Ajax updates. 4 years of production use (2021–2024) with 10+ version iterations. Supports multi-team assignments, live comment syncing, and status tracking.

`PHP` `MySQL` `jQuery` `Bootstrap` `DataTables` `Ajax`

[GitHub](https://github.com/giaphutran12/Whiteboard)

---

### [Build Launch Iterate](https://buildlaunchiterate.vercel.app/) — Company Website
> Marketing site for my dev studio. Process, services, and why you should hire us.

Landing page with Framer Motion animations, service comparison, methodology breakdown, and CTAs. Serverless PostgreSQL backend via Neon.

`Next.js 15` `React 19` `Neon PostgreSQL` `Framer Motion` `Tailwind CSS`

[Live Site](https://buildlaunchiterate.vercel.app/) • [GitHub](https://github.com/giaphutran12/buildlaunchiterate)

---

## 🏆 Leadership

**Led 8 BCIT interns → 2nd place at ISSP Expo 2025**

Built an AI call analysis app from scratch. The wild part? None of them knew Next.js or TypeScript 3 months prior. They normalized a nightmare dataset (200 rows × 220k columns of 10-year manual entries) into clean, queryable data. Result: <10ms queries, modern dashboard, AI-powered call insights for sales teams.

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=giaphutran12&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub Stats" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=giaphutran12&theme=tokyonight&hide_border=true" alt="GitHub Streak" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=giaphutran12&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" />
</p>

---

## 🛠 Tech Stack

**Languages:** TypeScript • JavaScript • Python • Rust • SQL • C++ • PHP

**Frontend:** Next.js • React • Tailwind CSS • shadcn/ui • Three.js • GSAP • Framer Motion

**Backend:** FastAPI • Prisma • tRPC • Inngest • Node.js • Sanity CMS

**AI/ML:** Claude API • Google Vertex AI • Gemini • OpenAI • AWS Bedrock • PyTorch • ONNX Runtime • Pinecone • MediaPipe • YOLOv8 • OpenCV • RAG

**Infrastructure:** Vercel • Supabase • Neon PostgreSQL • Redis • Stripe • E2B • WebAssembly

---

## 📫 Let's Connect

Building something interesting? I'm always down to chat.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/edwardtran123)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://edwardtran.ca)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:giaphutran012@gmail.com)

---

<p align="center">
  <i>I don't do LeetCode. I build products.</i>
</p>
