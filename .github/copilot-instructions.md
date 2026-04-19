# GitHub Copilot Instructions

This repository is an Angular 20 application with a zoneless runtime and a minimal workspace structure.

## Guidelines

- Prefer changes that preserve the existing architecture and file layout.
- Keep code aligned with Angular best practices and TypeScript conventions.
- Do not introduce new frameworks unless explicitly requested.
- Avoid modifying configuration files unless necessary for the requested task.
- Use concise, actionable suggestions and edits.
- Prioritize zoneless patterns: use signals, computed values, and effects over zone-based change detection.
- Favor standalone components and avoid NgModules where possible.
- Ensure async operations use RxJS observables or Angular's async pipe.

## Repository context

- Main application entry: `src/main.ts`
- App component: `src/app/app.ts`
- Routes and configuration are defined in `src/app/app.routes.ts`, `src/app/app.config.ts`
- Styling is in `src/styles.scss` and `src/app/app.scss`

## When editing

- Include only the minimal required changes.
- Add comments sparingly and only where helpful.
- Do not add generated or temporary files.
- Use Angular CLI for scaffolding new components, services, or guards.
- Validate changes by running `ng build` and `ng test`.
