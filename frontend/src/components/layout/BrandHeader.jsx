import React from "react";
import { useIntl } from "react-intl";
import AppIconTile from "../ui/AppIconTile";

export default function BrandHeader({
  title,
  subtitle,
  onBrandClick = () => {},
}) {
  const intl = useIntl();

  return (
    <header className="flex flex-col items-center justify-center gap-2 text-center">
      <button
        type="button"
        onClick={onBrandClick}
        className="rounded-2xl focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155DFC]/40 focus-visible:ring-offset-2 focus-visible:ring-offset-transparent"
        aria-label="Go to SecureBank home"
      >
        <AppIconTile aria-label={intl.formatMessage({ id: "appIconTile.ariaLabel" })} />
      </button>

      <h1 className="text-[30px] leading-9 font-bold tracking-[0.3955px] text-[#101828]">
        {title}
      </h1>
      <p className="text-[16px] leading-6 font-normal tracking-[-0.3125px] text-[#4A5565]">
        {subtitle}
      </p>
    </header>
  );
}