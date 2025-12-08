# Agentage - Development Instructions

> **"Agents should be as simple as writing a README, as portable as a Docker container, and as shareable as an npm package."**

## **Ecosystem Overview**

| Project | Description | Links |
|---------|-------------|-------|
| **[@agentage/sdk](https://github.com/agentage/agentkit)** | TypeScript SDK with builder pattern | [npm](https://www.npmjs.com/package/@agentage/sdk) |
| **[@agentage/cli](https://github.com/agentage/cli)** | NPM-like CLI for managing agents | [npm](https://www.npmjs.com/package/@agentage/cli) |
| **[Desktop](https://github.com/agentage/desktop)** | Electron app for visual agent management | [releases](https://github.com/agentage/desktop/releases) |
| **[Web](https://github.com/agentage/web)** | Website + Backend API (Next.js + Express + MongoDB) | [agentage.io](https://agentage.io) |
| **[agentage.io](https://agentage.io)** | Registry & platform | [docs](https://docs.agentage.io) |

## **Project Agreements**

- Default branch: `master`
- GitHub org: `agentage`
- Branch names: `feature/*`, `bugfix/*`, `hotfix/*`, `setup-*`
- Commits: `feat:`, `fix:`, `chore:` (max 72 chars)
- Verifications: `npm run verify` (type-check + lint + build + test)

## **Release Strategy**

- 🎯 **MINIMAL FIRST**: Simple, focused features
- 🚫 **No Over-Engineering**: Focus on core workflows
- ⚡ **Essential Only**: Run, edit, list, publish agents

## **Rules**

- 📊 Use icons/tables for structured output
- 📁 NO extra docs unless explicitly asked
- 🐙 GitHub org: `agentage`
- ⚡ Prefer function calls over terminal commands
- 📂 Source code in `src/` directory

## **Coding Standards**

### TypeScript

- 🚫 No `any` type - explicit types always
- 📤 Named exports only (no default exports)
- 📏 Files <200 lines, functions <20 lines
- 🔄 Functional: arrow functions, async/await, destructuring
- 🏗️ Interfaces over classes
- ✅ ESM modules (`type: "module"`)

### React

- ⚛️ Function components only (no class components)
- 🪝 Custom hooks for shared logic
- 📦 Props interfaces for all components
- 🎨 CSS variables for theming

### Naming

- **Interfaces**: `AgentConfig`, `AppConfig`, `IpcChannels`
- **Types**: `AppState`, `RunResult`
- **Components**: `AgentList.tsx`, `AgentRunner.tsx`
- **Files**: `*.service.ts`, `*.schema.ts`, `*.types.ts`, `*.test.ts`

## **Tech Stack**

- **Language**: TypeScript 5.3+ (strict mode)
- **Framework**: Electron 33+
- **UI**: React 18+ (strict mode)
- **Bundler**: Vite 6+
- **Validation**: Zod
- **Testing**: Jest 30+ with ts-jest
- **E2E**: Playwright
- **Linting**: ESLint 9+ (flat config)
- **Formatting**: Prettier
- **Package Manager**: npm

## **Node Requirements**

- Node.js >= 20.0.0
- npm >= 10.0.0

## **Architecture Patterns**

### Main Process (Electron)

```typescript
// IPC handler registration
ipcMain.handle('agents:list', async () => listAgents());
ipcMain.handle('agents:run', async (_event, name, prompt) => runAgent(name, prompt));
```

### Preload (Context Bridge)

```typescript
// Expose safe API to renderer
contextBridge.exposeInMainWorld('agentage', {
  agents: {
    list: () => ipcRenderer.invoke('agents:list'),
    run: (name, prompt) => ipcRenderer.invoke('agents:run', name, prompt),
  },
});
```

### Renderer (React)

```typescript
// Use exposed API
const agents = await window.agentage.agents.list();
```

## **Workspace Structure**

### Web (`agentage/web`) - Monorepo

```
packages/
  shared/             # Shared types & services
    types/            # TypeScript type definitions
  backend/            # Express.js API
    src/
      routes/         # API endpoints (agents/, auth/, health/)
      services/       # Business logic (agent, jwt, oauth, user)
      middleware/     # Auth middleware
      collections/    # MongoDB collections
  frontend/           # Next.js app
    src/
      app/            # App router pages
      components/     # UI components
      lib/            # Utilities
```

### Desktop (`agentage/desktop`) - Electron

```
src/
  main/               # Electron main process
    index.ts          # App entry, window creation
    preload.ts        # Context bridge (IPC)
    ipc/              # IPC handler registration
    services/         # Business logic
  renderer/           # React app (UI)
    main.tsx          # React entry
    App.tsx           # Main component
    components/       # UI components
    hooks/            # Custom React hooks
    pages/            # Page components
    styles/           # CSS files
  shared/             # Shared types & schemas
    schemas/          # Zod validation schemas
    types/            # TypeScript type definitions
```

### CLI (`agentage/cli`) - Standalone

```
src/
  cli.ts              # CLI entry point (Commander.js)
  index.ts            # Package exports
  commands/           # Command handlers
    init.ts           # Create new agent
    run.ts            # Execute agent
    list.ts           # Show agents
    publish.ts        # Upload to registry
    install.ts        # Download from registry
    search.ts         # Query registry
    login.ts          # Authenticate
    logout.ts         # Clear auth
    whoami.ts         # Show current user
    update.ts         # Update CLI
  services/           # API services
    auth.service.ts   # Authentication
    registry.service.ts # Registry API
  schemas/            # Zod validation schemas
  types/              # TypeScript types
  utils/              # Utility functions
```

### AgentKit (`agentage/agentkit`) - SDK Monorepo

```
packages/
  core/               # @agentage/core - Types & interfaces
  sdk/                # @agentage/sdk - Agent builder
    src/
      agent.ts        # agent() builder function
      tool.ts         # tool() factory function
      types/          # SDK types
  model-openai/       # @agentage/model-openai - OpenAI adapter
```

## **Scripts**

All packages support:

- `npm run dev` - Start dev (renderer + main)
- `npm run build` - Build TypeScript + Vite
- `npm run type-check` - TypeScript validation
- `npm run lint` - ESLint check
- `npm run lint:fix` - Auto-fix linting
- `npm run test` - Run Jest tests
- `npm run test:watch` - Watch mode
- `npm run test:coverage` - Coverage report
- `npm run verify` - All checks
- `npm run clean` - Clean build artifacts
- `npm run package` - Cross-platform packaging

## **Quality Gates**

- ✅ Type check must pass
- ✅ Linting must pass (no warnings)
- ✅ All tests must pass
- ✅ Coverage >= 70% (branches, functions, lines, statements)
- ✅ Build must succeed

## **Security**

- 🔒 Context isolation enabled
- 🔒 Node integration disabled in renderer
- 🔒 Preload scripts for safe IPC
- 🔒 Validate all user input with Zod
- 🔒 No secrets in repo (use `~/.agentage/config.json`)
