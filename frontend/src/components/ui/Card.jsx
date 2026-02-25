import React from "react";
import { useIntl } from "react-intl";
import cx from "../utils/cx";

export default function Card({ children, className }) {
  const intl = useIntl();

  return (
    <section
      className={cx(
        "w-full rounded-[14px] bg-white border border-[#e5e7eb]",
        "shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]",
        className
      )}
      aria-label={intl.formatMessage({ id: "card.ariaLabel" })}
    >
      {children}
    </section>
  );
}