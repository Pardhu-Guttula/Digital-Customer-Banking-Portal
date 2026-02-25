import React from "react";
import { useIntl } from "react-intl";

function noop() {}

export default function PrimaryButton({ label, disabled, onClick = noop, type = "submit" }) {
  const intl = useIntl();
  const resolvedLabel = label ?? intl.formatMessage({ id: "primaryButton.label" });

  return (
    <button
      type={type}
      disabled={disabled}
      onClick={onClick}
      className="h-11 w-full rounded-lg bg-[#030213] text-[14px] font-medium leading-5 tracking-[-0.1504px] text-white shadow-sm hover:bg-black focus:outline-none focus:ring-2 focus:ring-[#155DFC]/30 disabled:cursor-not-allowed disabled:opacity-60"
    >
      {resolvedLabel}
    </button>
  );
}