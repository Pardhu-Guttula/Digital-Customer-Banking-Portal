import React from "react";
import { useIntl } from "react-intl";

export default function PrimaryButton({
  children,
  disabled,
  onClick = () => {},
  type = "button",
}) {
  const intl = useIntl();

  return (
    <button
      type={type}
      disabled={disabled}
      onClick={onClick}
      className="h-11 w-full rounded-lg bg-[#030213] text-white text-[14px] leading-5 font-medium tracking-[-0.1504px] shadow-sm hover:bg-[#070625] disabled:opacity-60 disabled:cursor-not-allowed focus:outline-none focus:ring-4 focus:ring-[#030213]/20"
    >
      {children}
    </button>
  );
}