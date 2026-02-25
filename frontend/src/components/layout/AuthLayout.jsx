import React from "react";
import { useIntl } from "react-intl";

export default function AuthLayout({ children }) {
  const intl = useIntl();

  return (
    <main
      className="min-h-screen w-full px-4 sm:px-6 flex flex-col items-center justify-center"
      style={{
        backgroundImage:
          "linear-gradient(145.03869956590015deg, rgb(239, 246, 255) 0%, rgb(255, 255, 255) 50%, rgb(239, 246, 255) 100%)",
      }}
    >
      {children}
    </main>
  );
}