import React from "react";
import { useIntl } from "react-intl";

export default function PrimaryButton({ label, onClick = () => {}, ariaLabel }) {
  const intl = useIntl();

  const resolvedLabel = label || intl.formatMessage({ id: "common.continue" });

  return (
    <button
      type="button"
      aria-label={ariaLabel || resolvedLabel}
      onClick={onClick}
      className="inline-flex h-[34px] w-full items-center justify-center rounded-[8px] bg-[#030213] text-center text-[14px] font-medium leading-[20px] tracking-[-0.1504px] text-white transition-colors hover:bg-[#0b0d1a] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30"
    >
      {resolvedLabel}
    </button>
  );
}