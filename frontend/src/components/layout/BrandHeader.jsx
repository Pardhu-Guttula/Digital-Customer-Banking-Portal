import React from "react";
import { useIntl } from "react-intl";
import AppIconTile from "../ui/AppIconTile";

export default function BrandHeader({
  title,
  subtitle,
  iconMode = "lucide",
}) {
  const intl = useIntl();

  const resolvedTitle = title ?? intl.formatMessage({ id: "brandHeader.title" });
  const resolvedSubtitle = subtitle ?? intl.formatMessage({ id: "brandHeader.subtitle" });

  return (
    <header className="flex flex-col items-center justify-center gap-2 text-center">
      <AppIconTile icon={iconMode} alt={intl.formatMessage({ id: "brandHeader.iconAlt" })} />
      <h1 className="text-[30px] font-bold leading-9 tracking-[0.3955px] text-[#101828]">
        {resolvedTitle}
      </h1>
      <p className="text-base font-normal leading-6 tracking-[-0.3125px] text-[#4A5565]">
        {resolvedSubtitle}
      </p>
    </header>
  );
}