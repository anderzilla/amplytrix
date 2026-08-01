# syntax=docker/dockerfile:1.7
FROM node:24.14.1-alpine AS base
ENV PNPM_HOME=/pnpm
ENV PATH=$PNPM_HOME:$PATH
RUN corepack enable
WORKDIR /workspace

FROM base AS build
COPY . .
RUN pnpm install --frozen-lockfile
RUN pnpm --filter @amplytrix/web build

FROM node:24.14.1-alpine AS runtime
ENV NODE_ENV=production
ENV PORT=8080
RUN apk upgrade --no-cache \
  && rm -rf /usr/local/lib/node_modules/npm /usr/local/lib/node_modules/corepack \
  && rm -f /usr/local/bin/npm /usr/local/bin/npx /usr/local/bin/corepack /usr/local/bin/pnpm /usr/local/bin/pnpx \
  && addgroup -S app \
  && adduser -S -G app -u 10001 app
WORKDIR /app
COPY --from=build --chown=app:app /workspace/apps/web/.next/standalone ./
COPY --from=build --chown=app:app /workspace/apps/web/.next/static ./apps/web/.next/static
USER 10001
EXPOSE 8080
CMD ["node", "apps/web/server.js"]
