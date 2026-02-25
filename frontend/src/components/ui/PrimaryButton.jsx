import React from "react";
import { useIntl } from "react-intl";
import cn from "../utils/cx";

function noop() {}

export default function PrimaryButton({
  children,
  disabled,
  loading,
  onClick = noop,
  type = "submit",
}) {
  const intl = useIntl();

  return (
    <button
      type={type}
      disabled={disabled || loading}
      onClick={onClick}
      className={cn(
        "h-11 w-full rounded-lg bg-[#030213] text-center text-[14px] font-medium leading-5 tracking-[-0.1504px] text-white",
        "transition-colors hover:bg-[#0b0a22] active:bg-[#05041a]",
        "disabled:cursor-not-allowed disabled:opacity-60",
        "focus:outline-none focus:ring-2 focus:ring-[#155dfc]/25"
      )}
      aria-label={typeof children === "string" ? children : "Continue"}
    >
      {loading ? intl.formatMessage({ id: "primaryButton.continuing" }) : children}
    </button>
  );
}