import type { NextConfig } from 'next';
import path from 'node:path';

const securityHeaders = [
  {
    key: 'Content-Security-Policy',
    value: "default-src 'self'; frame-ancestors 'none'; object-src 'none'; base-uri 'self'",
  },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
];

const config: NextConfig = {
  output: 'standalone',
  poweredByHeader: false,
  turbopack: { root: path.resolve(__dirname, '../..') },
  // Next.js requires this configuration hook to return a Promise.
  // eslint-disable-next-line @typescript-eslint/require-await
  async headers() {
    return [{ source: '/(.*)', headers: securityHeaders }];
  },
};
export default config;
