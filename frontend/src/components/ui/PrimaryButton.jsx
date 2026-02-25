import React from "react";
import { useIntl } from "react-intl";

export default function PrimaryButton({ label, disabled, onClick = () => {} }) {
  useIntl();

  return (
    <button
      type="submit"
      disabled={disabled}
      onClick={onClick}
      className="h-11 w-full rounded-lg bg-[#030213] text-[14px] font-medium leading-5 tracking-[-0.1504px] text-white shadow-sm transition-colors hover:bg-[#0B0D1A] disabled:cursor-not-allowed disabled:opacity-60 focus:outline-none focus:ring-2 focus:ring-[#030213]/20"
    >
      {label}
    </button>
  );
}