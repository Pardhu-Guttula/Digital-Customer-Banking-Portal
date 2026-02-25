import React from "react";
import { useIntl } from "react-intl";

export default function IconTile({ tone = "green", icon: IconComp }) {
  useIntl();

  const toneStyles =
    tone === "green"
      ? "bg-[#F0FDF4] text-[#22C55E]"
      : tone === "blue"
        ? "bg-[#EFF6FF] text-[#3B82F6]"
        : "bg-[#FAF5FF] text-[#A855F7]";

  return (
    <div className={`flex h-[40px] w-[40px] items-center justify-center rounded-[10px] ${toneStyles}`}>
      <IconComp aria-hidden="true" className="h-[18px] w-[18px]" />
    </div>
  );
}