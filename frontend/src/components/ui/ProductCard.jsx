import React from "react";
import { useIntl } from "react-intl";

import IconTile from "./IconTile";
import StatusPill from "./StatusPill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  id,
  icon,
  iconBg,
  iconColor,
  badgeLabel,
  title,
  description,
  ctaLabel,
  ctaAriaLabel,
  onCta = () => {},
}) {
  const intl = useIntl();

  const resolvedCtaLabel =
    ctaLabel || intl.formatMessage({ id: "common.applyNow" });

  return (
    <article className="flex flex-col rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-4">
      <div className="flex items-start justify-between">
        <IconTile icon={icon} bgColor={iconBg} iconColor={iconColor} />
        <StatusPill label={badgeLabel} />
      </div>

      <div className="mt-3">
        <h3 className="text-[18px] font-medium leading-[28px] tracking-[-0.4395px] text-[#0a0a0a]">
          {title}
        </h3>
        <p className="mt-1.5 text-[14px] font-normal leading-[22px] tracking-[-0.2px] text-[#717182]">
          {description}
        </p>
      </div>

      <div className="mt-4">
        <PrimaryButton
          label={resolvedCtaLabel}
          ariaLabel={
            ctaAriaLabel ||
            intl.formatMessage(
              { id: "productsForYou.applyAriaLabel" },
              { ctaLabel: resolvedCtaLabel, title }
            )
          }
          onClick={() => onCta(id)}
        />
      </div>
    </article>
  );
}