import React from "react";
import { useIntl } from "react-intl";

export default function PrimaryButton({ label, onClick = () => {}, fullWidth = true }) {
  const intl = useIntl();
  const resolvedLabel = label ?? intl.formatMessage({ id: "common.applyNow" });

  return (
    <button
      type="button"
      onClick={onClick}
      className={[
        "h-[36px] rounded-[8px] bg-[#030213] px-4 text-center text-[14px] font-medium leading-[20px] tracking-[-0.1504px] text-white",
        "transition-colors hover:bg-[#0b0a1f] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30",
        fullWidth ? "w-full" : "",
      ].join(" ")}
    >
      {resolvedLabel}
    </button>
  );
}