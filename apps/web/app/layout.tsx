import type { ReactNode } from 'react';

export const metadata = {
  title: 'Amplytrix Foundation',
  description: 'Architecture foundation status',
};

export default function RootLayout({ children }: Readonly<{ children: ReactNode }>) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
