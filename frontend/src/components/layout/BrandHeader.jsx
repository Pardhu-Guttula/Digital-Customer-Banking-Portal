import React from "react";
import { useIntl } from "react-intl";
import { Landmark } from "lucide-react";

function noop() {}

export default function BrandHeader({
  title,
  subtitle,
  onBrandClick = noop,
  useRemoteIcon = false,
  imgIcon,
}) {
  const intl = useIntl();

  return (
    <header className="flex flex-col items-center justify-center gap-2 text-center">
      <button
        type="button"
        onClick={onBrandClick}
        className="grid h-16 w-16 place-items-center rounded-2xl bg-[#155dfc] shadow-sm transition-transform hover:scale-[1.02] active:scale-[0.99]"
        aria-label="SecureBank Portal home"
      >
        {useRemoteIcon ? (
          <img src={imgIcon} alt="SecureBank icon" className="h-8 w-8" />
        ) : (
          <Landmark className="h-8 w-8 text-white" aria-hidden="true" />
        )}
      </button>

      <h1 className="text-center text-[30px] font-bold leading-9 tracking-[0.3955px] text-[#101828]">
        {title ?? intl.formatMessage({ id: "brandHeader.title" })}
      </h1>

      <p className="text-center text-[16px] font-normal leading-6 tracking-[-0.3125px] text-[#4a5565]">
        {subtitle ?? intl.formatMessage({ id: "brandHeader.subtitle" })}
      </p>
    </header>
  );
}