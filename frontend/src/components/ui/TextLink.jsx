import React from "react";
import { useIntl } from "react-intl";

export default function TextLink({ children, onClick = () => {}, href = "#" }) {
  const intl = useIntl();

  return (
    <a
      href={href}
      onClick={(e) => {
        e.preventDefault();
        onClick();
      }}
      className="text-[14px] leading-5 tracking-[-0.1504px] text-[#155dfc] hover:underline underline-offset-2 focus:outline-none focus:ring-4 focus:ring-[#155dfc]/15 rounded"
    >
      {children}
    </a>
  );
}