import React from "react";
import { useIntl } from "react-intl";
import cx from "../utils/cx";

export default function TextLink({ children, onClick = () => {}, href = "#", className }) {
  const intl = useIntl();

  return (
    <a
      href={href}
      onClick={(e) => {
        e.preventDefault();
        onClick();
      }}
      className={cx(
        "text-[#155dfc] text-[14px] leading-5 tracking-[-0.1504px]",
        "hover:underline focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155dfc]/40 rounded-sm",
        className
      )}
      aria-label={intl.formatMessage({ id: "textLink.ariaLabel" })}
    >
      {children}
    </a>
  );
}