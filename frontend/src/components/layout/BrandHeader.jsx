import React from "react";
import { useIntl } from "react-intl";
import { Landmark } from "lucide-react";

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
        className="grid h-16 w-16 place-items-center rounded-2xl bg-[#155DFC] shadow-sm transition-colors hover:bg-[#0F4FE6] focus:outline-none focus:ring-2 focus:ring-[#155DFC]/30"
        aria-label="SecureBank home"
      >
        <Landmark className="h-8 w-8 text-white" aria-hidden="true" />
      </button>

      <h1 className="text-[30px] font-bold leading-9 tracking-[0.3955px] text-[#101828]">
        {title ??
          intl.formatMessage({
            id: "brandHeader.title",
          })}
      </h1>
      <p className="text-base leading-6 tracking-[-0.3125px] text-[#4A5565]">
        {subtitle ??
          intl.formatMessage({
            id: "brandHeader.subtitle",
          })}
      </p>
    </header>
  );
}