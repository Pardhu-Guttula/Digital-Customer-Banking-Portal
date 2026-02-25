import React from "react";
import { useIntl } from "react-intl";
import AppIconBadge from "../ui/AppIconBadge";

export default function BrandHeader({
  title,
  subtitle,
  useRemoteIcon = false,
  remoteIconSrc,
}) {
  const intl = useIntl();

  return (
    <header className="flex flex-col items-center justify-center gap-2 text-center">
      <AppIconBadge useRemoteIcon={useRemoteIcon} remoteIconSrc={remoteIconSrc} />
      <h1 className="text-[30px] leading-9 font-bold text-[#101828] tracking-[0.3955px]">
        {title ?? intl.formatMessage({ id: "brandHeader.title" })}
      </h1>
      <p className="text-[16px] leading-6 text-[#4a5565] tracking-[-0.3125px]">
        {subtitle ?? intl.formatMessage({ id: "brandHeader.subtitle" })}
      </p>
    </header>
  );
}