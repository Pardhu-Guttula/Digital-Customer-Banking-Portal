import React from "react";
import { useIntl } from "react-intl";

export default function AuthShell({ children }) {
  const intl = useIntl();

  return (
    <main
      className="min-h-dvh w-full flex items-center justify-center px-4 py-10 sm:py-12"
      style={{
        backgroundImage:
          "linear-gradient(145.03869956590015deg, rgb(239, 246, 255) 0%, rgb(255, 255, 255) 50%, rgb(239, 246, 255) 100%)",
      }}
      aria-label={intl.formatMessage({ id: "authShell.ariaLabel" })}
    >
      {children}
    </main>
  );
}