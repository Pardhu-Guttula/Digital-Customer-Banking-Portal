import React from "react";
import { useIntl } from "react-intl";

export default function BadgePill({ text }) {
  const intl = useIntl();
  const resolvedText = text ?? intl.formatMessage({ id: "badgePill.text" });

  return (
    <span className="inline-flex items-center justify-center rounded-[8px] bg-[#eceef2] px-[9px] py-[3px] text-[12px] font-medium leading-[16px] tracking-[-0.1px] text-[#030213]">
      {resolvedText}
    </span>
  );
}