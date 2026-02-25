import React from "react";
import { useIntl } from "react-intl";
import { Landmark } from "lucide-react";

function noop() {}

export default function GlobalHeader({
  title,
  subtitle,
  onBrandClick = noop,
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "globalHeader.title" });
  const resolvedSubtitle =
    subtitle ?? intl.formatMessage({ id: "globalHeader.subtitle" });

  return (
    <header className="flex flex-col items-center justify-center gap-2 text-center">
      <button
        type="button"
        onClick={onBrandClick}
        aria-label="SecureBank Portal"
        className="grid h-16 w-16 place-items-center rounded-2xl bg-[#155dfc] text-white shadow-sm transition-transform hover:scale-[1.02] active:scale-[0.99]"
      >
        <Landmark className="h-8 w-8" aria-hidden="true" />
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