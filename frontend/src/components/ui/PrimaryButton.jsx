import React from "react";
import { useIntl } from "react-intl";

export default function PrimaryButton({
  children,
  disabled = false,
  onClick = () => {},
}) {
  useIntl(); // required by spec for components with text; children text is provided by parent

  return (
    <button
      type="submit"
      disabled={disabled}
      onClick={onClick}
      className="h-11 w-full rounded-lg bg-[#030213] text-[14px] font-medium leading-5 tracking-[-0.1504px] text-white shadow-sm transition-opacity hover:opacity-95 disabled:cursor-not-allowed disabled:opacity-60 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30"
    >
      {children}
    </button>
  );
}