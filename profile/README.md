# Agentage

> **AI agents as simple as functions**

Build AI agents with minimal code—just composable functions.

## 📦 Projects

**[agentkit](https://github.com/agentage/agentkit)** – Complete toolkit (core + SDK + CLI)

```typescript
const agent = agent('reviewer').model('gpt-4').tools([github]);
await agent.send('Review PR #123');
```
