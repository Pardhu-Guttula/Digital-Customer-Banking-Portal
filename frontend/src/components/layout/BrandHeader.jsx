import React from "react";
import { useIntl } from "react-intl";
import { Landmark } from "lucide-react";

export default function BrandHeader({
  title,
  subtitle,
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "brandHeader.title" });
  const resolvedSubtitle =
    subtitle ?? intl.formatMessage({ id: "brandHeader.subtitle" });

  return (
    <header className="flex flex-col items-center justify-center gap-2 text-center">
      <div className="h-16 w-16 rounded-2xl bg-[#155dfc] flex items-center justify-center shadow-sm">
        <Landmark aria-hidden="true" className="h-8 w-8 text-white" />
      </div>

      <h1 className="text-[30px] leading-9 font-bold tracking-[0.3955px] text-[#101828]">
        {resolvedTitle}
      </h1>

      <p className="text-base leading-6 tracking-[-0.3125px] text-[#4a5565]">
        {resolvedSubtitle}
      </p>
    </header>
  );
}