# Agentage

> **AI agents as simple as functions, portable as containers, shareable as packages**

---

## 🎯 Vision

Build AI agents with minimal code. No classes, no complexity—just simple, composable functions used everywhere.

---

## 📦 Projects

### [agentkit](https://github.com/agentage/agentkit)
Complete toolkit for building AI agents (core + SDK + CLI in one monorepo)

```typescript
const agent = agent('reviewer').model('gpt-4').tools([github]);
await agent.send('Review PR #123');
```

```bash
agent run reviewer "Check this code"
```

### [agentage.io](https://agentage.io)
Main landing page for Agent marketplace, docs, and playground

---

## 🤝 Contributing

**Rules**: Named exports • No `any` • <200 lines/file • Functional patterns

📖 [Docs](https://agentage.io/docs) • 💬 [Discussions](https://github.com/orgs/agentage/discussions) • 🐛 [Issues](https://github.com/agentage/agentkit/issues)

---

**MIT © 2025 • Built by [@vreshch](https://github.com/vreshch)**