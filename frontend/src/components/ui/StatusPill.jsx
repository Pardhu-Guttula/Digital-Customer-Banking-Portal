import React from "react";
import { useIntl } from "react-intl";

export default function StatusPill({ label }) {
  const intl = useIntl();

  return (
    <span className="inline-flex items-center justify-center rounded-[8px] bg-[#eceef2] px-[9px] py-[3px] text-[12px] font-medium leading-[16px] text-[#030213]">
      {label || intl.formatMessage({ id: "common.status" })}
    </span>
  );
}