import React from "react";
import { useIntl } from "react-intl";
import { Building2 } from "lucide-react";

export default function BrandHeader({
  title,
  subtitle,
  onBrandClick = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "brandHeader.title" });
  const resolvedSubtitle =
    subtitle ?? intl.formatMessage({ id: "brandHeader.subtitle" });

  return (
    <header className="flex flex-col items-center justify-center gap-2 text-center">
      <button
        type="button"
        onClick={onBrandClick}
        className="grid h-16 w-16 place-items-center rounded-2xl bg-[#155dfc] shadow-sm transition-transform hover:scale-[1.02] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155dfc]/40"
        aria-label="SecureBank Portal home"
      >
        <span className="sr-only">
          {intl.formatMessage({ id: "brandHeader.srOnly" })}
        </span>
        <Building2 className="h-8 w-8 text-white" aria-hidden="true" />
      </button>

      <h1 className="text-[30px] font-bold leading-9 tracking-[0.3955px] text-[#101828]">
        {resolvedTitle}
      </h1>
      <p className="text-base leading-6 tracking-[-0.3125px] text-[#4a5565]">
        {resolvedSubtitle}
      </p>
    </header>
  );
}