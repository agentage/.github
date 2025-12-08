# Agentage

> **"Agents should be as simple as writing a README, as portable as a Docker container, and as shareable as an npm package."**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 Vision

Make AI agents:

- ✅ **Simple** to create (YAML/Markdown definition)
- ✅ **Portable** (works everywhere)
- ✅ **Shareable** (NPM-like registry)
- ✅ **Synchronized** (cross-platform)

---

## 📦 Ecosystem

| Project | Description | Status |
|---------|-------------|--------|
| **[@agentage/sdk](https://github.com/agentage/agentkit)** | TypeScript SDK with builder pattern | [![npm](https://img.shields.io/npm/v/@agentage/sdk.svg)](https://www.npmjs.com/package/@agentage/sdk) |
| **[@agentage/cli](https://github.com/agentage/cli)** | NPM-like CLI for managing agents | [![npm](https://img.shields.io/npm/v/@agentage/cli.svg)](https://www.npmjs.com/package/@agentage/cli) |
| **[Desktop](https://github.com/agentage/desktop)** | Electron app for visual agent management | 🚧 In Progress |
| **[Web](https://github.com/agentage/web)** | Website + Backend API (Next.js + Express + MongoDB) | 🚧 In Progress |
| **[agentage.io](https://agentage.io)** | Registry & platform | 🚧 In Progress |

---

## 🚀 Quick Start

### SDK (Programmatic)

```typescript
import { agent, tool } from '@agentage/sdk';

const assistant = agent('assistant')
  .model('gpt-4', { temperature: 0.7 })
  .instructions('You are a helpful assistant')
  .tools([searchTool]);

const result = await assistant.send('Help me with this task');
```

### CLI (Terminal)

```bash
# Install
npm install -g @agentage/cli

# Create & run agent
agent init my-assistant
agent run my-assistant "What is TypeScript?"

# Registry commands
agent publish              # Publish to registry
agent install user/agent   # Install from registry
agent search "code review" # Search registry
```

---

## 🏗️ Architecture


```
┌─────────────────────────────────────────────────────┐
│              Desktop App (Electron)                 │
│   React UI → IPC → Embedded CLI Engine              │
└────────────────────────┬────────────────────────────┘
                         │
    ┌────────────────────┼────────────────────┐
    ▼                    ▼                    ▼
┌──────────┐      ┌──────────────┐      ┌──────────┐
│ Registry │      │ GitHub Repos │      │  Local   │
│ API      │      │  (.agent.md) │      │  Files   │
└──────────┘      └──────────────┘      └──────────┘
```

---

## 📋 Agent Definition (`.agent.md`)

```yaml
---
name: code-reviewer
model: gpt-4
temperature: 0.7
tools:
  - github
---

You are an expert code reviewer.
Review code for bugs, security issues, and best practices.
```

---

## 🔗 Links

| Resource | URL |
|----------|-----|
| Documentation | [docs.agentage.io](https://docs.agentage.io) |
| Registry | [agentage.io](https://agentage.io) |
| SDK Reference | [API Docs](https://github.com/agentage/agentkit/blob/master/docs/api-reference.md) |

---

## 📄 License

MIT © [Agentage](https://agentage.io)